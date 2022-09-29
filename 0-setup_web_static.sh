#!/usr/bin/env bash
# Script that configures Nginx server with some folders and files

# Install Nginx if it not already installed
apt-get -y update
apt-get -y install nginx
service nginx start

# Create the folders
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link
ln -fs /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the folder
chown -R ubuntu /data/
chown -R :ubuntu /data/

# Update the Nginx configuration to server
sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
service nginx restart
exit 0

