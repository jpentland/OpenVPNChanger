# Install Apache2
```
sudo apt-get install apache2
```

# Enable CGI
Enable CGI mode
```
sudo a2enmod cgi
```
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

# Add dependecies
`index.py` depends on:
* `yattag`
* `cgi`
* `os`
* `subprocess`

Install them using `pip` or any other tool
```
sudo pip yattag
```

# Enable OpenVPN Server
copy `index.py` and `openvpn_setup` to `/var/www/cgi` and make them executable
```
chmod +x index.py openvpn_setup
```
Add openvpn_setup to visudo so it can be run without a sudo password:
```
sudo visduo
```
adding the lines at the end of the file
```
#no pass for openvpn_setup
ALL ALL = NOPASSWD: /var/www/cgi/openvpn_setup
```
Optional: Modify the `openvpn_setup` script to suit your openvpn setup.
Current script is called with a location of a OpenVPN configuration file as an argument.
