
from netmiko import ConnectHandler

# Define device information
cisco_switch = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.100',  # Replace with your switch IP
    'username': 'admin',
    'password': 'password',  # Consider using getpass() for security
    'secret': 'enable_password',  # Optional: for privileged exec mode
}

# VLAN configuration data (from image)
vlans = {
    10: "Management",
    20: "LAN",
    50: "WLAN",
    70: "VoIP",
    199: "Blackhole"
}

# Establish SSH connection
connection = ConnectHandler(**cisco_switch)
connection.enable()

# Configure VLANs
commands = []
for vlan_id, vlan_name in vlans.items():
    commands.append(f"vlan {vlan_id}")
    commands.append(f"name {vlan_name}")

output = connection.send_config_set(commands)
print("✅ VLANs configured successfully:\n")
print(output)

# Save configuration
connection.save_config()

# Disconnect session
connection.disconnect()
