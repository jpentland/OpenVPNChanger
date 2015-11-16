#!/usr/bin/env python

from yattag import Doc
from yattag import indent
import cgi
import os
import subprocess

query = cgi.parse()

OPENVPN_PATH = "/etc/openvpn/"
OPENVPN_SETUP_SCRIPT = os.getcwd() + "/openvpn_setup"

def set_server(server):
    command = "sudo %s %s" % (OPENVPN_SETUP_SCRIPT, OPENVPN_PATH + server)
    try:
        return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()
    except:
        return "Failed"

# get current server
try:
    out = subprocess.check_output(['pgrep', '-af', 'openvpn'])
    config_path = (out.split("\n")[0]).split("--config ")[1]
    config_file = config_path.split("/")
    current_server = config_file[-1]
    doc, tag, text = Doc(
        defaults = {'server': current_server}
    ).tagtext()
except:
    current_server = 'none'
    doc, tag, text = Doc(
        defaults = {}
    ).tagtext()

doc.asis('<!DOCTYPE html>')

with tag('html'):
    with tag('body'):
        with tag('form', action = ""):
            with tag('br'):
                text('Default OpenVPN configuration path: ' + OPENVPN_PATH)
            with tag('br'):
                text('Curent server: ' + current_server)
            with tag('br'):
                text('')
            with tag('label'):
                text("Select a VPN server")
            with doc.select(name = 'server'):
                lst = os.listdir(OPENVPN_PATH)
                lst.sort()
                for file in lst:
                    if file.endswith(".conf"):
                        with doc.option(value = file):
                            text(file.split(".conf")[0])
            doc.stag('input', type = "submit", value = "Set")

        if query.has_key('server'):
            server = query['server'][0]
            info = set_server(server).split("\n")
            for openvpn_info in info:
                with tag('br'):
                     text(openvpn_info)

print "Content-type: text/html\n"

result = indent(
    doc.getvalue(),
    indentation = '    ',
    newline = '\r\n'
)
print(result)