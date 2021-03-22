# Шестая программа

import re
import glob
from ipaddress import IPv4Interface

def classify(s):

    m = re.match("^ ip address ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+) ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)", s)
    if m:
        return{"ip":IPv4Interface(str(m.group(1)) + "/" + str(m.group(2)))}

    m = re.match("^interface (.+)", s)
    if m:
        return{"int":m.group(1)}

    m = re.match("^hostname (.+)", s)
    if m:
        return {"host":m.group(1)}

    return("Unclassified",)

ip_address = []
interface = []
hosts = []

for f_name in glob.glob("/Users/aa.morzherin/Documents/p4ne_training/config_files/*.txt"):
    with open(f_name) as f:
        for cur_line in f:
            cl = classify(cur_line)
            if "ip" in cl: ip_address.append(cl)
            if "int" in cl: interface.append(cl)
            if "host" in cl: hosts.append(cl)

print(ip_address)
print(interface)
print(hosts)