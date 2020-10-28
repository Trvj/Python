import os   
import nmap3
import pandas as pd
import json

ipaddy = []

nm = nmap3.Nmap()

nm_scan = nmap3.NmapScanTechniques()

scanresults = nm_scan.nmap_ping_scan('192.168.0.*')#list of dictionaries
for element in scanresults:
    #element = dictionary
    ipaddresses = element['addresses'][0]['addr']
    ipaddy.append(ipaddresses)

def get_ip_info(ip):
    results = nm_scan.nmap_ping_scan(ip)
    results = results[0]
    ipaddress = results['addresses'][0]['addr']
    macaddress = results['addresses'][1]['addr']
    vendor = results['addresses'][1]['vendor']
    mydict = {'ips': ipaddress, 'macaddress': macaddress, 'vendor': vendor}
    return mydict


print(get_ip_info('192.168.0.99'))
