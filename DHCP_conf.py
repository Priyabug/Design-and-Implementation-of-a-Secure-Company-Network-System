from netmiko import ConnectHandler

cisco_router = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.1',  # Replace with actual router IP
    'username': 'admin',
    'password': 'password',
    'secret': 'enable_password'
}

commands = [
    "ip dhcp excluded-address 192.168.10.1 192.168.10.10",
    "ip dhcp pool LAN_POOL",
    "network 192.168.10.0 255.255.255.0",
    "default-router 192.168.10.1",
    "dns-server 8.8.8.8 8.8.4.4",
    "lease 7"
]

connection = ConnectHandler(**cisco_router)
connection.enable()

print("🔧 Configuring DHCP on Cisco device...")
output = connection.send_config_set(commands)
print(output)

connection.save_config()
connection.disconnect()
print("✅ DHCP Configuration applied and saved.")
