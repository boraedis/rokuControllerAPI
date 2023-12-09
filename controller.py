from flask import Flask
import requests
import ssdpy
from pprint import pprint

app = Flask(__name__)
USN = 'uuid:roku:ecp:YN00X0747615'

RokuIP = 'http://192.168.86.33:8060/'

@app.route("/press/home")
def pressHome():
    global RokuIP
    if not RokuIP:
        getRokuIP()

    res = requests.post(RokuIP + 'keypress/Home')
    return {
        'statusCode': 200
    }

@app.route("/press/back")
def back():
    global RokuIP
    if not RokuIP:
        getRokuIP()

    res = requests.post(RokuIP + 'keypress/Back')
    return {
        'statusCode': 200
    }

@app.route("/press/poweron")
def powerOn():
    global RokuIP
    if not RokuIP:
        getRokuIP()

    res = requests.post(RokuIP + 'keypress/PowerOn')
    return {
        'statusCode': 200
    }

@app.route("/press/poweroff")
def powerOff():
    global RokuIP
    if not RokuIP:
        getRokuIP()

    res = requests.post(RokuIP + 'keypress/PowerOff')
    return {
        'statusCode': 200
    }

@app.route("/press/volumeup/<amount>")
def volumeUp(amount):
    global RokuIP
    if not RokuIP:
        getRokuIP()

    for i in range(amount):
        res = requests.post(RokuIP + 'keypress/VolumeUp')
    return {
        'statusCode': 200
    }

@app.route("/press/volumedown/<amount>")
def volumeDown(amount):
    global RokuIP
    if not RokuIP:
        getRokuIP()

    for i in range(amount):
        res = requests.post(RokuIP + 'keypress/VolumeDown')
    return {
        'statusCode': 200
    }

@app.route("/press/mute")
def mute(amount):
    global RokuIP
    if not RokuIP:
        getRokuIP()

    for i in range(amount):
        res = requests.post(RokuIP + 'keypress/VolumeMute')
    return {
        'statusCode': 200
    }

# @app.route('/launch/<channel_id>')
# def launch(channel_id):
#     res = requests.post(RokuIP + 'launch/' + channel_id)
#     return {
#         'statusCode': 200
#     }

# def setupConnection():
    

def getRokuIP():
    global RokuIP
    HOST = '239.255.255.250'
    # PORT = '1900'

    client = ssdpy.SSDPClient()
    devices = client.m_search("roku:ecp")
    if len(devices) == 0:
        return False
    RokuIP = devices[0]
    return RokuIP