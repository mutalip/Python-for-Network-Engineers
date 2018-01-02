#!/usr/bin/env python3
#########################################
# Runs the "sh bgp neig" command
import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('192.168.122.72', 'david', 'cisco')
iosvl2.open()
 
ios_output = iosvl2.get_facts()
print (json.dumps(bgp_neighbors, indent=4))
 
bgp_neighbors = iosvl2.get_bgp_neighbors()
print (json.dumps(bgp_neighbors, indent=4))
 
iosvl2.close()
