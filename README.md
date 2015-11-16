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

Edit default configuration file
```
sudo nano /etc/apache2/sites-enabled/000-default.conf
```
Add before `ServerAdmin webmaster@localhost`:
```
        <Directory /var/www/cgi>
            Options +ExecCGI
            DirectoryIndex index.py
        </Directory>
        AddHandler cgi-script .py
```
and change `DocumentRoot` to `/var/www/cgi`
Restart apache2 service
```
sudo service apache2 restart`
```

## Install yattag

Yattag is a python library for generating HTML or XML in a "pythonic way".

```
sudo apt-get install python-pip
sudo pip install yattag
```

## Enable OpenVPN Server
copy `index.py` and `openvpn_setup` to `/var/www/cgi` and make them executable
```
chmod +x index.py openvpn_setup
```
Add openvpn_setup to visudo so it can be run without a sudo password:
```
sudo visudo
```
adding the lines at the end of the file
```
##no pass for openvpn_setup
ALL ALL = NOPASSWD: /var/www/cgi/openvpn_setup
```
Optional: Modify the `openvpn_setup` script to suit your openvpn setup.
Current script is called with a location of a OpenVPN configuration file as an argument.
