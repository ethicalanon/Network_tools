
#!/usr/bin/env python

import subprocess
import optparse
import re


def change_mac(mac,macAddress):
	subprocess.call(["ifconfig", mac, "down"])

	subprocess.call(["ifconfig", mac, "hw", "ether", macAddress])

	subprocess.call(["ifconfig", mac, "up"])

def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-i", "--macInterface", dest="mac", help="Enter a mac address you would like to change")
	parser.add_option("-m", "--macAddress", dest="macAddress", help="Enter a mac address which consists of six octals seperated by columns")
	(options, arguments) = parser.parse_args()
	if not options.mac:
        	parser.error("No mac supplied")
	elif not options.macAddress:
        	parser.error("No mac address supplied")        


	return parser.parse_args()

def get_current_mac(mac):

        ifconfig_result = subprocess.check_output(["ifconfig",mac])
        search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result)
        
        if search_result:
		return search_result.group(0)

        else: 
                print("[-] Could not read mac address")


(options, arguments) = get_arguments()

change_mac(options.mac,options.macAddress)
if get_current_mac(options.mac) == options.macAddress:
	print("Mac address changed to: " + options.macAddress)
