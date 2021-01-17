#!/bin/sh

set -o errexit

# check directory for hexo
checkdir() {
    if [[ `ls -A /hexo|wc -w` -eq "0" ]]  #判断hexo目录是否为空
    then
        git clone -b $TAG $GITSITE /hexo
    echo "git clone over"
    fi
}

setgitnpm() {
    if [[ ! -z ${PROXY} ]]
    then
        npm config set proxy ${PROXY}
        npm config set https-proxy ${PROXY}
        git config --global http.proxy ${PROXY}
        git config --global https.proxy ${PROXY}
    elif [[ ! -z ${GITUSER} && ! -z ${GITEMAIL} ]]
    then
        git config --gloable user.name ${GITUSER}
        git config --gloable user.email ${GITEMAIL}
    fi
    touch /setgitnpm.tmp
}
# install hexo package
installhexo() {
    cd /hexo
    npm install
    npm audit fix
    touch /installhexo.tmp
}

# init config
initsshconf() {
    if [[ ! -f "/sshconfig.tmp" ]]
    then
        echo "init config ..."
        echo "root:$PASSWORD" | chpasswd
        echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config
        echo 'Port 22' >> /etc/ssh/sshd_config
        ssh-keygen -A
        touch /sshconfig.tmp
    else
        echo "ssh config is ok!"
    fi
}

# start ssh server
startssh() {
    checkdir
    if [[ ! -f /setgitnpm.tmp ]]
    then
        setgitnpm
    elif [[ ! -f /installhexo.tmp ]]
    then
        installhexo
    fi
    initsshconf
    echo "ssh server starting..."
    /usr/sbin/sshd -D
}

startssh
