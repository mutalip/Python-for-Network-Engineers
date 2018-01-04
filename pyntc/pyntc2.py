######################################################
import json
from pyntc import ntc_device as NTC
iosvl2 = NTC(host='XXXXXXXXXXXXXX', username='XXXX', password='XXXXXXX', device_type='cisco_ios_ssh')
iosvl2.open()
 
ios_run = iosvl2.running_config
 
HOST = 'XXXXXXXXXXXXX'
saveoutput = open('switch' + HOST, 'w')
saveoutput.write(ios_run)
saveoutput.close
