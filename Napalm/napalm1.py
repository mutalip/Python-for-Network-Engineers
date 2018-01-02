#!/usr/bin/env python3
########################################################
#Simple napalm code to access switch and get basic information about the device.
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver(''XXXX','XXXX','XXXXXXXXXXXXXXXXXXXXXX')
iosvl2.open()
ios_output =  iosvl2.get_facts()
print (ios_output)

