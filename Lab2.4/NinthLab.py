# Девятая программа

import requests, json, pprint

from flask import Flask
from flask import render_template, jsonify

top = "sandboxapicem.cisco.com"
tok = "sandboxapic.cisco.com"

def new_ticket():
    url = 'https://' + tok + '/api/v1/ticket'
    payload = {"username": "devnetuser",
               "password": "Cisco123!"
               }
    header = {"content-type": "application/json"}

    response = requests.post(url, data=json.dumps(payload),
                             headers=header, verify=False)

    return response.json()['response']['serviceTicket']

def get_host(ticket):
    url = "https://" + top + "/api/v1/host"

    header = {"content-type": "application/json",
              "X-Auth-Token":ticket}

    response = requests.get(url, headers=header, verify=False)

    return response.json()

def get_device(ticket):
    url = "https://" + tok + "/api/v1/network-device"

    header = {"content-type": "application/json",
              "X-Auth-Token": ticket}

    response = requests.get(url, headers=header, verify=False)

    return response.json()

def get_topology(ticket):
    url = "https://" + top + "/api/v1/topology/physical-topology"

    header = {"content-type": "application/json",
              "X-Auth-Token": ticket}

    response = requests.get(url, headers=header, verify=False)

    return response.json()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("topology.html")

@app.route("/api/topology")
def topology():
    ticket = new_ticket()
    return jsonify(get_topology(ticket)['response'])

if __name__ == '__main__':

    ticket = new_ticket()


    print("hosts = ")
    pprint.pprint(get_host(ticket))

    print("devices = ")
    pprint.pprint(get_device(ticket))

    print("topology = ")
    pprint.pprint(get_topology(ticket))

    app.run(debug=True)