#!/bin/sh
confile="/aria2/conf/aria2.conf"
sessionfile="/aria2/conf/arai2.session"
dhtfile="/aria2/conf/dht.dat"

if [ ! -f "${confile}" ]; then
    echo "Error" && exit 0
fi

/usr/bin/aria2c --conf-path=$confile --dir=/aria2/downloads \
--rpc-secret=${SECRET}