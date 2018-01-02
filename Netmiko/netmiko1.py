####################################################################
#Simple netmiko example
#SSH to switch and run the commnad"sh ip int brie"

#!/usr/bin/env python3

from netmiko import ConnectHandler
import time

iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.3.5',
    'username': 'admin',
    'password': 'B.h.d.c.switcH',
}


net_connect = ConnectHandler(**iosv_l2)
print ("connected")
output = net_connect.send_command("sh ip int brie")
fp = open("ntoutput", "w")
fp.write(str(output))
print(fp)
