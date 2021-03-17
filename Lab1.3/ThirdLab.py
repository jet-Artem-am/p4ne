#Третья программа

from pysnmp.hlapi import *

def snmp_exception(Excepion): pass

def print_snmp(a):
    for result in a:
        errorIndication, errorStatus, errorIndex, varBinds = result
        if errorIndication:
            print(errorIndication)
            raise snmp_exception
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
            raise snmp_exception
        else:
            for varBind in varBinds:
                print(varBind)
                print('='.join([x.prettyPrint() for x in varBind]))
try:
    a = getCmd(SnmpEngine(), CommunityData('public', mpModel=0), UdpTransportTarget(('10.31.70.107', 161)),ContextData(), ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))
    print_snmp(a)

    b = nextCmd(SnmpEngine(), CommunityData('public', mpModel=0), UdpTransportTarget(('10.31.70.107', 161)), ContextData(), ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2')),lexicographicMode=False)
    print_snmp(b)

except:
    print('Error-exception')