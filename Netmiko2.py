  GNU nano 2.7.4                                                                   File: netmiko2.py                                                                             

#!/usr/bin/env python3
############################################
#SSH to multiple switches

from netmiko import ConnectHandler
import time

############################################
#Switch infor
iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': 'X.X.X.X',
    'username': 'XXXXX',
    'password': 'XXXXX',
}

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': 'X.X.X.X',
    'username': 'XXXX',
    'password': 'XXXX',
}

iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': 'XXXXXX',
    'username': 'XXXXX',
    'password': 'XXXXX',
}

#print (iosv_l2_s3['ip'])
#print (iosv_l2_s2['ip'])
#print (iosv_l2_s1['ip'])


all_devices = [iosv_l2_s1, iosv_l2_s2, iosv_l2_s3]

for devices in all_devices:
        net_connect = ConnectHandler(**devices)
        print ("connected to ", devices['ip'])

        output = net_connect.send_command("sh ip int brie\n")
        #net_connect.send_command("exit\n")
        #fp = open("ntoutput", "w")
        #fp.write(str(output))
        #print(fp)
        print (output)

