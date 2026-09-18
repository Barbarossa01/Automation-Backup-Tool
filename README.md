# Automation-Backup-Tool

A Python network automation script built with [Netmiko](https://github.com/ktbyers/netmiko) to manage devices that require multi-stage SSH logins (e.g., dropping from an underlying host Linux shell into a target vendor CLI mode).

---

## Overview

Some network appliances initially drop SSH connections into an underlying host Linux environment before requiring an explicit shell invocation command (like `cli`) to access the device configuration prompt.

This tool automates that transition using dynamic prompt pattern matching (`expect_string`), runs diagnostic commands, and captures raw configuration backups.

---

## Features

* **Multi-Shell Prompt Handling:** Manages prompt pattern changes when moving from Linux bash (`$`) to vendor CLI (`>`).
* **Automated Configuration Backup:** Fetches device configurations and writes clean, unformatted output to backup files.
* **Modular Function Structure:** Reusable Python functions for running environment diagnostics (`show_version`) and capturing state (`backup_device`).
* **Secure Credential Handling:** Designed to pull login parameters safely via environment variables or parameter dictionaries.

---

## Prerequisites

* **Python 3.8+**
* Dependencies:
  ```bash
  pip install netmiko
  ```
## Usage
Configure Environment Variables:
export NET_USER="your_username"
export NET_PASS="your_password"
Run the script: python main.py
