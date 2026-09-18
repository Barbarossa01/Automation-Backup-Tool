import os
from netmiko import ConnectHandler

# Fetch credentials securely from environment variables
USERNAME = os.getenv("NET_USER", "student")
PASSWORD = os.getenv("NET_PASS", "your_password")

# Example target device definitions
DEVICE_1 = {
    'device_type': 'linux',
    'host': '10.0.0.1',
    'username': USERNAME,
    'password': PASSWORD
}

DEVICE_2 = {
    'device_type': 'linux',
    'host': '10.0.0.2',
    'username': USERNAME,
    'password': PASSWORD
}


def show_version(device_dict):
    """Navigates from host shell to device CLI and retrieves version details."""
    connection = ConnectHandler(**device_dict)

    commands = ['pwd', 'cli', 'show version']
    for command in commands:
        if command != 'pwd':
            # Handle transition to the '>' CLI prompt
            output = connection.send_command(command, expect_string=r'>')
        else:
            output = connection.send_command(command)

        print(f"--- Output of '{command}' ---")
        print(output)

    connection.disconnect()


def backup_device(device_dict, backup_filename="device_backup.txt"):
    """Connects to target host, enters CLI shell, and saves configuration to disk."""
    connection = ConnectHandler(**device_dict)
    commands = ['cli', 'show configuration | display set | no-more']

    with open(backup_filename, "w") as file_handle:
        for command in commands:
            output = connection.send_command(command, expect_string=r'>')
            print(f"--- Executed: '{command}' ---")
            file_handle.write(f"--- Output of '{command}' ---\n")
            file_handle.write(f"{output}\n\n")

    connection.disconnect()


if __name__ == "__main__":
    # Example execution
    backup_device(DEVICE_1)
