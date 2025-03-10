from pysnmp.hlapi import *

def add_device(ip, community):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData(community),
               UdpTransportTarget((ip, 161)),
               ContextData(),
               ObjectType(ObjectIdentity('1.3.6.1.2.1.1.1.0')))  # sysDescr OID
    )

    if errorIndication:
        print(f"Error: {errorIndication}")
    elif errorStatus:
        print(f"Error: {errorStatus.prettyPrint()}")
    else:
        for varBind in varBinds:
            print(f'{varBind[0]} = {varBind[1]}')

if __name__ == "__main__":
    ip_address = "192.168.1.1"  # Replace with your device's IP address
    community_string = "public"  # Replace with your SNMP community string
    add_device(ip_address, community_string)
