
#!/usr/bin/env python3
import netmiko
import devices1

netmiko_exceptions = (netmiko.ssh_exception.NetMikoAuthenticationException,netmiko.ssh_exception.NetMikoTimeoutException)
devices = []
#with open('devices.json') as dev_file:
#       devices = json.load(dev_file)
devices  =  [devices1.s1, devices1.s2, devices1.s3]
for device in devices:
        try :
                connection  = netmiko.ConnectHandler(**device)
                print(connection.send_command('show clock'))
                connection.disconnect()

        except netmiko_exceptions as e:
                #print("Authentication Failed vvvv")
                print("failed to connect ", device['ip'], e)

