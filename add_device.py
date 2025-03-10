import requests
from requests.auth import HTTPBasicAuth
from pysnmp.hlapi import *

# Function to verify SNMP connectivity
def verify_snmp(ip, community):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData(community),
               UdpTransportTarget((ip, 161)),
               ContextData(),
               ObjectType(ObjectIdentity('1.3.6.1.2.1.1.1.0')))  # sysDescr OID
    )

    if errorIndication:
        print(f"Error: {errorIndication}")
        return False
    elif errorStatus:
        print(f"Error: {errorStatus.prettyPrint()}")
        return False
    else:
        for varBind in varBinds:
            print(f'{varBind[0]} = {varBind[1]}')
        return True

# Function to add device to SolarWinds
def add_device_to_solarwinds(ip, community, solarwinds_url, username, password):
    if verify_snmp(ip, community):
        node_data = {
            "Caption": ip,
            "IPAddress": ip,
            "EngineID": 1,
            "ObjectSubType": "SNMP",
            "SNMPVersion": 2,
            "Community": community
        }

        response = requests.post(
            f"{solarwinds_url}/SolarWinds/InformationService/v3/Json/Invoke/Orion.Nodes",
            json=node_data,
            auth=HTTPBasicAuth(username, password),
            verify=False
        )

        if response.status_code == 200:
            print(f"Device {ip} added successfully to SolarWinds.")
        else:
            print(f"Failed to add device {ip} to SolarWinds. Status code: {response.status_code}")
            print(response.text)

if __name__ == "__main__":
    ip_address = "192.168.1.100"  # Replace with your device's IP address
    community_string = "public"  # Replace with your SNMP community string
    solarwinds_url = "https://your-solarwinds-server:17778"  # Replace with your SolarWinds server URL
    username = "admin"  # Replace with your SolarWinds username
    password = "password"  # Replace with your SolarWinds password

    add_device_to_solarwinds(ip_address, community_string, solarwinds_url, username, password)
