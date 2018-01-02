
#!/usr/bin/env python3

import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('192.168.3.5','admin','B.h.d.c.switcH')
iosvl2.open()
ios_output =  iosvl2.get_facts()
#print (ios_output)
#print (json.dumps(ios_output, indent=4))



ios_output = iosvl2.ping('google.com')
print ( json.dumps(ios_output, sort_keys=True, indent=4))

iosvl2.close()


