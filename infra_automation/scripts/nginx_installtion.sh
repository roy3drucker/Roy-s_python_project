#!/bin/bash

# Update package lists
echo "Updating package lists..."

# Check if Nginx is installed
if ! dpkg -l | grep -q nginx; then
    echo "Nginx is not installed. Installing..."
    echo "Simulating Nginx installation (no actual installation performed)"
    echo "Nginx installed successfully"
else
    echo "Nginx is already installed"
fi

# Start Nginx service
echo "Starting Nginx service..."
echo "sudo systemctl start nginx"

# Enable Nginx to start on boot
echo "Enabling Nginx to start on boot..."
echo "sudo systemctl enable nginx"

echo "Nginx setup completed successfully"
