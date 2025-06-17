from netmiko import ConnectHandler

# Device details (replace with your own)
cisco_device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.100',  # Replace with your switch IP
    'username': 'admin',
    'password': 'your_password',
    'secret': 'enable_password',  # Optional
}

# Interfaces to bundle (example: GigabitEthernet0/1 and 0/2)
interfaces = ["GigabitEthernet0/1", "GigabitEthernet0/2"]
port_channel_number = 1

# Build config commands
commands = []
for intf in interfaces:
    commands += [
        f"interface {intf}",
        "channel-group 1 mode active",
        "no shutdown",
    ]

# Configure Port-Channel interface
commands += [
    f"interface Port-channel{port_channel_number}",
    "switchport",
    "switchport mode trunk",  # or 'access' based on your need
    "no shutdown"
]

# Connect to the device and apply the config
net_connect = ConnectHandler(**cisco_device)
net_connect.enable()

print("🔧 Applying EtherChannel (LACP) configuration...")
output = net_connect.send_config_set(commands)
print(output)

# Save the configuration
net_connect.save_config()
net_connect.disconnect()
print("✅ Configuration complete and saved.")
