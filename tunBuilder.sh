#!/bin/sh

sudo ip tuntap add name $1 mode tun
sudo ip addr add $2 dev $1
sudo ip link set $1 up


sudo sysctl -w net.ipv4.ip_forward=1

sudo iptables -t nat -A POSTROUTING -s $2 ! -o $1 -j MASQUERADE



