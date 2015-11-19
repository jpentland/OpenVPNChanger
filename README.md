# About
Simple web interface using python cgi for switching between VPN Configurations

# Installation

## Install Apache2
```
sudo apt-get install apache2
```

## Enable CGI
Enable CGI mode
```
sudo a2enmod cgi
```

*Note: This may result in the message "Your MPM seems to be threaded. Selecting cgid instead of cgi."*

## Install yattag

Yattag is a python library for generating HTML or XML in a "pythonic way".

```
sudo apt-get install python-pip
sudo pip install yattag
```

## Enable OpenVPN Server

Install files:

```
	sudo cp vpn.py /usr/lib/cgi-bin
	sudo cp openvpn_setup /usr/local/bin
	sudo cp -r www/* /var/www/

```
Add openvpn_setup to visudo so it can be run without a sudo password:
```
sudo visudo
```
adding the lines at the end of the file
```
##no pass for openvpn_setup
ALL ALL = NOPASSWD: openvpn_setup
```

## Copy vpn configuration
Create a directory called /etc/openvpn-configs
```
mkdir /etc/openvpn-configs
```

Copy all your ".ovpn" files to this directory:
```
cp /path/to/files/*.ovpn /etc/openvpn-configs
```

## Create credentials file
*Note: This app currently assumes ovpn files use auth-user-pass*

Create a new file /etc/openvpn/vpn-login continaning your VPN username and password:

E.g:
```
someone@example.com
hunter2
```

