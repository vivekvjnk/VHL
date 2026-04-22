#!/bin/bash
# Docker VHL Network Setup Script
# This script ensures the vhl-network is created and ready for Docker Compose

set -e

NETWORK_NAME="vhl-network"
NETWORK_DRIVER="bridge"

echo "=========================================="
echo "VHL Docker Network Setup"
echo "=========================================="
echo ""
echo "Network Name: $NETWORK_NAME"
echo "Driver: $NETWORK_DRIVER"
echo ""

# Check if network already exists
if docker network ls | grep -q "$NETWORK_NAME"; then
    echo "✓ Network '$NETWORK_NAME' already exists"
    
    # Get network details
    echo ""
    echo "Network Details:"
    docker network inspect "$NETWORK_NAME" | grep -E '"Name"|"Driver"|"Containers"' || true
else
    echo "Creating network '$NETWORK_NAME'..."
    docker network create \
        --driver "$NETWORK_DRIVER" \
        "$NETWORK_NAME"
    
    echo "✓ Network '$NETWORK_NAME' created successfully"
fi

echo ""
echo "=========================================="
echo "Setup Complete!"
echo "=========================================="
echo ""
echo "You can now run:"
echo "  cd vhl-runtime && docker-compose up"
echo "  cd vhl-agent-backend && docker-compose up"
echo ""
echo "To remove the network later (when all containers are stopped):"
echo "  docker network rm $NETWORK_NAME"
echo ""
