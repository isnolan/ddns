#!/usr/bin/env python
#-*- coding:utf-8 -*-

import httplib, urllib, ssl
import socket
import time

params = dict(
    login_token="YOUR_LOGIN_TOKEN", # replace with your login token
    format="json",
    domain_id=YOUR_DOMAIN_ID, # replace with your domain_od, can get it by API Domain.List
    record_id=YOUR_RECORD_ID, # replace with your record_id, can get it by API Record.List
    sub_domain="sj", # replace with your sub_domain
    record_line="默认",
)
current_ip = None

def ddns(ip):
    params.update(dict(value=ip))
    ssl._create_default_https_context = ssl._create_unverified_context
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/json"}
    conn = httplib.HTTPSConnection("dnsapi.cn")
    conn.request("POST", "/Record.Ddns", urllib.urlencode(params), headers)
    
    response = conn.getresponse()
    #print response.status, response.reason
    data = response.read()
    #print data
    conn.close()
    return response.status == 200

def getip():
    conn = httplib.HTTPConnection("members.3322.org")
    conn.request('GET', '/dyndns/getip', '', {'user-agent':'ddns for dnspod'})
    ip = conn.getresponse().read()
    print ip
    conn.close()
    return ip

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

if __name__ == '__main__':
    while True:
        try:
            ip = getip()
            #print ip
            if current_ip != ip:
                if ddns(ip):
                    current_ip = ip
        except Exception, e:
            print e
            pass
        time.sleep(30)
