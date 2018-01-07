#!/usr/bin/env python3
import jason
######################################################
#Simple napalm code to print infromation in human readable format using jason library


from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('192.168.x.x','admin','***********')
iosvl2.open()
ios_output =  iosvl2.get_facts()
#print (ios_output)
print (json.dumps(ios_output, indent=4))

ios_output = iosvl2.get_interfaces()
print ( json.dumps(ios_output, sort_keys=True, indent=4)

ios_output = iosvl2.get_interfaces_counters()
print json.dumps(ios_output, sort_keys=True indent=4))

iosvl2.close()
