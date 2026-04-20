#!/bin/bash
DOMAIN="readme-gen.link"

# Install certbot if not present
if ! command -v certbot &> /dev/null; then
    sudo dnf install -y certbot python3-certbot-nginx 2>/dev/null || \
    (sudo amazon-linux-extras enable epel 2>/dev/null; sudo yum install -y certbot python3-certbot-nginx) || \
    sudo pip3 install certbot certbot-nginx
fi

# Request certificate (skips if already exists)
sudo certbot --nginx -d $DOMAIN --non-interactive --agree-tos -m $CERTBOT_EMAIL --redirect

# Auto-renew via cron
echo "0 3 * * * root certbot renew --quiet" | sudo tee /etc/cron.d/certbot-renew
