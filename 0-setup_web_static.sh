#!/usr/bin/env bash
# Script that configures Nginx server with some folders and files
apt-get -y update
apt-get -y install nginx
service nginx start
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "test html :)" | sudo tee /data/web_static/releases/test/index.html
ln -fs /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu /data/
chown -R :ubuntu /data/
sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
service nginx restart
exit 0

