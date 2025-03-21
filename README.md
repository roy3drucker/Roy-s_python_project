# Machine Provisioning Script

## Overview
This Python script automates the setup and validation of machine configurations, ensuring they meet predefined requirements. It also provides an option to install Nginx on the machines.

## Features
- Accepts user input to define new machines
- Validates machine configurations using JSON schema
- Prevents duplicate IP addresses
- Saves machine configurations to a JSON file
- Runs a Bash script to install Nginx (optional)
- Logs all activities for troubleshooting

## Prerequisites
- Python 3.13.2
- Required Python packages:
  - `json`
  - `logging`
  - `subprocess`
  - `jsonschema`
- A valid `configs/instances.json` file (if not present, create an empty JSON array `[]`)
- A Bash script `Scripts/nginx_installtion.sh` for Nginx installation

## Installation
1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
2. Install dependencies from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the script:
   ```bash
   python main.py
   ```
2. Enter machine details when prompted, including:
   - Machine name
   - IP address
   - Operating system (e.g., Ubuntu, CentOS)
   - CPU configuration (e.g., 2vCPU)
   - RAM size (GB)
3. The script will validate the configuration and save it if valid.
4. Optionally, install Nginx by selecting "yes" when prompted.
5. Logs are stored in `logs/provisioning.log` for debugging.


## Troubleshooting
- If a validation error occurs, check `logs/provisioning.log`.
- If the script cannot execute the Bash script, ensure it has execution permissions:
  ```bash
  chmod +x Scripts/nginx_installtion.sh
  ```