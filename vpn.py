#!/usr/bin/env python
# This file provides a cgi interface to set a VPN configuration
# assuming files in /etc/nordvpn
#
# TODO: Make this configurable
#
# Place in /usr/lib/cgi-bin
#
# Example usage: "curl http://server/cgi-bin/vpn.py?request=list"
# See below for commands

import cgi
import os
import sys
import subprocess
import json

OVPN_FILES_PATH = "/etc/nordvpn/"
OPENVPN_PATH = "/etc/openvpn"
OVPN_SETUP = "openvpn_setup"
OVPN_FILE_EXT = ".ovpn"
CONF_FILE_EXT = ".conf"
CONTENT_TYPE = "application/json"

commandList = []

# This is a decorator which appends function to commandList
# so it will be seen by main()
def command(fn):
    commandList.append(fn)
    return fn

# Get list of files with given extension in dir, removing extension
def listDirExt(path, ext):
	lst = os.listdir(path)
	return [baseName for baseName, _ext in map(os.path.splitext, lst)
					if _ext == ext]

# Print content type header
def print_content_type():
	print "Content-Type: %s" % CONTENT_TYPE
	print

# listVpn: List all ovpn files in ovpn files path (with extension removed)
# eg: {'vpns' : ['vpn1', 'vpn2'] }
@command
def list(data):
	vpns = sorted(listDirExt(OVPN_FILES_PATH, OVPN_FILE_EXT))
	return json.dumps({"vpns": vpns})

# getCurrent: Just return current vpn
# eg: {'vpn' : 'vpn1'}
@command
def getCurrent(data):
	current = listDirExt(OPENVPN_PATH, CONF_FILE_EXT)

	if len(current) != 1:
		res = "error"
	else:
		res = current[0]

	return json.dumps({"vpn" : res})

# set: Set the VPN, return output of openvpn_setup script
@command
def setVpn(data):

	try:
		vpn = data['vpn'][0]
	except:
		return json.dumps({"result" : "mising param: vpn"})

	ovpn_file = os.path.join(OVPN_FILES_PATH, vpn + OVPN_FILE_EXT)
	command = "sudo %s %s" % (OVPN_SETUP, ovpn_file)
	print "command:", command

	try:
		process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
		result = process.stdout.read()
	except:
		result = "failed to exec %s" % OPEVPN_PATH

	return json.dumps({"result" : result})

def main():
	print_content_type()
	data = cgi.parse()

	if "request" not in data:
			sys.exit(1)

	for command in commandList:
		if data["request"][0] == command.__name__:
			print command(data)
			sys.exit(0)

	sys.exit(1)

if __name__=="__main__": main()
