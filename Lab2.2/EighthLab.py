# Восьмая программа

from flask import Flask, jsonify
import json
import sys
import re
import glob
import pprint

hosts = {}

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    s = """
        Help:
        /configs - сведения об именах всех хостов из конфигурационных файлов
        /config/hostname - сведения о всех IP-адресах хоста
    """
    return(s)

@app.route('/configs')
def hosts_info():
    r = []
    for n in hosts.keys():
        r.append(hosts[n]['name'])
    return jsonify(r)

@app.route('/configs/<hostname>')
def ip_info(hostname):
    for n in hosts.keys():
        if hosts[n]['name'] == hostname:
            return jsonify(hosts[n]['addresses'])
    return jsonify("Not found")

if __name__ == '__main__':

    for current_file_name in glob.glob("/Users/aa.morzherin/Documents/p4ne_training/config_files/*.txt"):
        hosts[current_file_name] = {}
        hosts[current_file_name]['addresses'] = []

        with open(current_file_name) as l:
            for current_line in l:
                m = re.match("hostname (.+)", current_line)
                if m:
                    hosts[current_file_name]['name'] = m.group(1)
                    continue
                m = re.match("ip address ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+) ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)", current_line)
                if m:
                    hosts[current_file_name]['addresses'].append({'ip': m.group(1), 'mask': m.group(2)})

pprint.pprint(hosts)
app.run(debug=True)