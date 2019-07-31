#!/usr/bin/env python

import scapy.all as scapy
import re
import argparse

def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("-t", "--target", dest="target", help="Enter target IP or IP range")
	options = parser.parse_args()
	return options

def scan(ip):
	arp_request = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_req_broad = broadcast/arp_request
	answered =scapy.srp(arp_req_broad,timeout=1)[0]

	client_list =[]
	for answer in answered:
		client_dict = {"ip":answer[1].psrc,"mac":answer[1].hwsrc}
		client_list.append(client_dict)
	return client_list

def print_list(list):
        print("\tIP\t\t\t\tMAC ADDRESS\t\t\t")
        print("\t-----------------------------------------------")
        for val in list:
                print("\t" + val["ip"] + "\t\t\t" + val["mac"])



target = get_args()

if target.target:
	result = scan(target.target)
	print_list(result)
else:
	print("No target IP entered")
