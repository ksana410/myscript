#!/bin/sh

set -o errexit

# check directory for hexo
if [ `ls -A /hexo|wc -w` -eq "0" ]
then
    git clone -b $TAG $GITSITE /hexo
    if [[ !-z ${PROXY} ]]
    then
        npm config set proxy ${PROXY}
        npm config set https-proxy ${PROXY}
        git config --global http.proxy ${PROXY}
        git config --global https.proxy ${PROXY}
    fi
    echo "git clone over"
fi

# install hexo package
cd /hexo
npm install

# init config
if [ ! -f "/tmp/sshconfig.tmp" ]
then
    echo "init config ..."
    echo "root:$PASSWORD" | chpasswd
    echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config
    echo 'Port 22' >> /etc/ssh/sshd_config
    ssh-keygen -A
    touch /tmp/sshconfig.tmp
else
    echo "ssh server will start!"
fi

# start ssh server
echo "ssh server starting..."
/usr/sbin/sshd -D
