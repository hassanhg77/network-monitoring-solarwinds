# network-monitoring-solarwinds
This repository contains a Python script to add network devices for monitoring using SNMP.

## Overview
This script demonstrates how to use SNMP to add network devices to SolarWinds for monitoring purposes. 

## Explanation
1. Importing the Library:
"from pysnmp.hlapi import *"
This line imports all necessary functions from the pysnmp.hlapi module, which provides high-level SNMP operations.

2. Defining the Function
"def add_device(ip, community):"
This defines a function named add_device that takes two parameters: ip (the IP address of the device) and community (the SNMP community string).

3. SNMP Get Command
"errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
           CommunityData(community),
           UdpTransportTarget((ip, 161)),
           ContextData(),
           ObjectType(ObjectIdentity('1.3.6.1.2.1.1.1.0')))) "

SnmpEngine(): Initializes the SNMP engine.
CommunityData(community): Specifies the community string for SNMP v1/v2c.
UdpTransportTarget((ip, 161)): Sets the target device’s IP address and port (161 is the default SNMP port).
ContextData(): Provides context information (empty for SNMP v1/v2c).
ObjectType(ObjectIdentity('1.3.6.1.2.1.1.1.0')): Specifies the OID (Object Identifier) for the sysDescr object, which contains a description of the device.

4.Error Handling:
" if errorIndication:
    print(f"Error: {errorIndication}")
elif errorStatus:
    print(f"Error: {errorStatus.prettyPrint()}")
else:
    for varBind in varBinds:
        print(f'{varBind[0]} = {varBind[1]}') "
        
errorIndication: Checks for general errors in the SNMP operation.
errorStatus: Checks for specific errors related to the SNMP request.
varBinds: Contains the retrieved SNMP data. If no errors occur, it prints the OID and its value.

5. Main Block:
   " if name == "main":            
    ip_address = "192.168.1.1"  # Replace with your device's IP address
    community_string = "public"  # Replace with your SNMP community string
    add_device(ip_address, community_string) "

   This block runs the add_device function if the script is executed directly. It sets the ip_address and community_string variables and calls the function.

Customization: 
IP Address: Replace "192.168.1.1" with the IP address of the device you want to monitor.
Community String: Replace "public" with the appropriate SNMP community string for your network.


