#Using pyntc get facts

import json
from pyntc import ntc_device as NTC
iosvl2 = NTC(host='192.168.x.x', username='', password='xx', device_type='cisco_ios_ssh')
iosvl2.open()

ios_output = iosvl2.facts
print (json.dumps(ios_output, indent=4))
 
iosvl2.close()
