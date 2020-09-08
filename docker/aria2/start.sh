#!/bin/sh
confile="/aria2/conf/aria2.conf"
sessionfile="/aria2/conf/arai2.session"
dhtfile="/aria2/conf/dht.dat"

if [ ! -f "$confile" ]; then
