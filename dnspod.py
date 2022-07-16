#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import http.client, urllib
import socket
import time

params = dict(
    login_token="YOUR_LOGIN_TOKEN", # replace with your login token
    format="json",
    domain_id=YOUR_DOMAIN_ID, # replace with your domain_od, can get it by API Domain.List
    record_id=YOUR_RECORD_ID, # replace with your record_id, can get it by API Record.List
    sub_domain="osx",
    record_line="默认",
)
current_ip = None

def ddns(ip):
    params.update(dict(value=ip))
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/json"}
    conn = http.client.HTTPSConnection("dnsapi.cn")
    conn.request("POST", "/Record.Ddns", urllib.parse.urlencode(params), headers)
    
    response = conn.getresponse()
    #print response.status, response.reason
    data = response.read()
    #print data
    conn.close()
    return response.status == 200

def getip():
    conn = http.client.HTTPConnection("members.3322.org")
    conn.request('GET', '/dyndns/getip', '', {'user-agent':'ddns for dnspod'})
    ip = conn.getresponse().read()
    print(ip)
    conn.close()
    return ip

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


if __name__ == '__main__':
    while True:
        try:
            # ip = getip()
            ip = get_ip_address()
            print(ip)
            if current_ip != ip:
                if ddns(ip):
                    current_ip = ip
        except Exception as e:
            print(e)
            pass
        time.sleep(30)

