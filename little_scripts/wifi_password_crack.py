import pywifi
import logging
import time
import chardet

pywifi.set_loglevel(logging.WARNING)
wifi = pywifi.PyWiFi().interfaces()[0]
wifi.scan()
time.sleep(3)
wifi_nets = wifi.scan_results()
for x in wifi_nets:
    print(x.ssid)
    print(chardet(x.ssid))