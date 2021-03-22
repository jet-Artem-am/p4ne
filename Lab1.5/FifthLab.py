# Пятая программа

import glob

ip_set = set()

for f_name in glob.glob("/Users/aa.morzherin/Documents/p4ne_training/config_files/*.txt"):
    with open(f_name) as a:
        for cur_line in a:
            if cur_line.find("ip address") == 1:
                ip_set.add(cur_line.replace("ip address", "").strip())

for n in ip_set:
    print(n)