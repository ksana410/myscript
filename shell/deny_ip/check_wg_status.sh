#!/usr/bin/env bash

# A script to check wireguard connection status!

ipaddr=$1

if [[ ! ping -c 1 -W 1 $ipaddr &> /dev/null ]]; then
    echo "Wireguard is down!"
    systemctl restart wg-quick@wg0
else
    echo "Wireguard is up!"
    exit 0
fi