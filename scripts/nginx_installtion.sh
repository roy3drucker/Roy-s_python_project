#!/bin/bash

# Update package lists
echo "Updating package lists..."
sudo apt update || { echo "Failed to update package lists"; exit 1; }

# Check if Nginx is installed
if ! dpkg -l | grep -q nginx; then
    echo "Nginx is not installed. Installing..."
    sudo apt install -y nginx || { echo "Failed to install Nginx"; exit 1; }
    echo "Nginx installed successfully."
else
    echo "Nginx is already installed."
fi

# Start Nginx service
echo "Starting Nginx service..."
sudo systemctl start nginx || { echo "Failed to start Nginx"; exit 1; }

# Enable Nginx to start on boot
echo "Enabling Nginx to start on boot..."
sudo systemctl enable nginx || { echo "Failed to enable Nginx"; exit 1; }

echo "Nginx setup completed successfully."
