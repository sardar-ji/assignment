#!/usr/bin/python3

#######################################################################################
# This script retrieves the status of the services i.e UP or DOWN.
# And Create a JSON object to a file named {serviceName}-status-{@timestamp}.json
# You can update the dictionary values i.e add other services name to check the status.
# If no service is installed and running, it will show status DOWN, otherwise UP.
########################################################################################

import os
import socket
import time
import json

#Create a dictionary with services name.
services_name = ('httpd','rabbitMQ', 'postgreSQL')

#Function which check service is UP or DOWN and return status.
def check_service_status(service_name):

    status = os.system('systemctl status ' + service_name
                       + ' > /dev/null')
    return status


def main():

    #For loop to check all the three services.
    for svc_name in services_name:
        #if condition call the function and get the status.    
        if check_service_status(svc_name) == 0:
            ts = time.time()
            up = {'host_name': "host1",
                  'service_name': svc_name, 'service_status': 'UP', 'time': ts}
            jsonString = json.dumps(up, indent=4)
            name = svc_name + '-status-' + str(ts) + '.json'
            with open(name, 'w') as outfile:
                json.dump(up, outfile, indent=4)
        else:
            ts = time.time()            
            down = {'service_name': svc_name, 'service_status': 'DOWN',
                    'host_name': "host1", 'time': ts}
            jsonString = json.dumps(down, indent=4)
            name = svc_name + '-status-' + str(ts) + '.json'
            with open(name, 'w') as outfile:
                json.dump(down, outfile, indent=4)


main()
