# Python Netmiko Lab

A Python project demonstrating network automation using Netmiko to connect to and manage Cisco routers via SSH.

## Overview

This project automates the retrieval of network interface information from a Cisco router using the Netmiko library. It connects to a Cisco IOS device via SSH, executes commands, and saves the output to a file.

## Features

- SSH connection to Cisco IOS devices
- Automated command execution
- Output saved to file for analysis
- Virtual environment support
- Automated setup script

## Prerequisites

- Python 3.x
- Network connectivity to the Cisco router (192.168.56.0/24 network)
- Cisco router with SSH enabled
- Ubuntu VM or Linux environment (for using the start.sh script)

## Installation

### Option 1: Using the automated script (Linux/Ubuntu)

```bash
chmod +x start.sh
./start.sh
```

The script will:
- Check and install Python3 if needed
- Create a virtual environment
- Install required dependencies
- Run the main script

### Option 2: Manual installation

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Configuration

### Router Configuration

The router must be configured with SSH access. Example configuration (from `setting.txt`):

```cisco
enable
conf t
hostname R1
ip domain-name lab.local
crypto key generate rsa modulus 2048
ip ssh version 2
username admin privilege 15 secret admin123
line vty 0 4
 transport input ssh
 login local
 exec-timeout 15 0
exit
interface FastEthernet0/0
 ip address 192.168.56.1 255.255.255.0
 no shutdown
exit
end
wr
```

### VM Network Configuration

Configure your Ubuntu VM's network (example in `setting.txt`):

```yaml
network:
  version: 2
  renderer: NetworkManager
  ethernets:
    ens32:
      addresses:
        - 192.168.56.10/24
      nameservers:
        addresses: [8.8.8.8, 1.1.1.1]
```

Apply the configuration:
```bash
sudo netplan apply
```

### Application Configuration

Edit `main.py` to update the device connection parameters:

```python
device = {
    'device_type': 'cisco_ios',
    'host': '192.168.56.1',      # Router IP address
    'username': 'admin',          # SSH username
    'password': 'admin123',       # SSH password
    'secret': 'enablepass',       # Enable password (if required)
}
```

## Usage

1. Ensure your router is powered on and accessible
2. Verify network connectivity:
   ```bash
   ping 192.168.56.1
   ```

3. Run the script:
   ```bash
   python main.py
   ```

4. The script will:
   - Connect to the router via SSH
   - Enter enable mode
   - Execute `show ip interface brief`
   - Save output to `interfaces.txt`
   - Display the output in the terminal

## Output

The script generates an `interfaces.txt` file containing the output of the `show ip interface brief` command, showing all network interfaces and their status.

## Project Structure

```
Python_Netmiko/
├── main.py                                           # Main Python script
├── requirements.txt                                  # Python dependencies
├── start.sh                                          # Automated setup script
├── router-c3725-adventerprisek9-mz.124-15.T14.image  # Cisco IOS image
├── interfaces.txt                                    # Output file (generated)
└── README.md                                         # This file
```

## Dependencies

- **netmiko**: Multi-vendor library to simplify Paramiko SSH connections to network devices

## Troubleshooting

### Connection Issues
- Verify the router IP address is correct and reachable
- Check that SSH is enabled on the router
- Ensure firewall rules allow SSH traffic
- Verify credentials are correct

### Authentication Failures
- Double-check username and password in `main.py`
- Ensure the user has privilege level 15 or appropriate permissions
- Verify the enable password if required

### Network Issues
- Test connectivity: `ping 192.168.56.1`
- Check VM network configuration: `ip addr show`
- Verify router interface is up: access router console and check interface status

## License

This is a lab project for educational purposes.

## Author

Network Automation Lab Project