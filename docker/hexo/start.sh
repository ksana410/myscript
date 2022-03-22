#!/bin/sh

# set -o errexit # Exit on error

# check directory for hexo
checkdir() {
    if [[ `ls -A /hexo/data|wc -w` -eq "0" ]]  #判断hexo目录是否为空
    then
        git clone -b ${TAG} ${GITSITE} /hexo/data  #克隆项目至本地目录
    echo "Git clone over"
    fi
}

# config git/npm proxy and user
setgitnpm() {
    if [[ ! -z ${PROXY} ]]
    then
        npm config set proxy ${PROXY}
        npm config set https-proxy ${PROXY}
        git config --global http.https://github.com.proxy ${PROXY}
        if [[ ! -z ${GITUSER} && ! -z ${GITEMAIL} ]]
        then
            git config --global user.name ${GITUSER}
            git config --global user.email ${GITEMAIL}
        fi
    else
        echo "Configuration is complete"
    fi
    touch /hexo/setgitnpm.tmp
}
# install hexo package
installhexo() {
    cd /hexo/data
    npm install
    npm audit fix --force
    touch /hexo/installhexo.tmp
    echo "Install hexo package over"
}

# init config
initsshconf() {
    if [[ ! -f "/hexo/sshconfig.tmp" ]]
    then
        echo "init config ..."
        echo "root:${PASSWORD}" | chpasswd  #设定ssh密码
        echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config
        echo 'Port 22' >> /etc/ssh/sshd_config
        if [[ ${PUB_KEY} ]]
        then
            echo "Add pub key ..."
            echo ${PUB_KEY} >> /root/.ssh/authorized_keys
            chmod 600 /root/.ssh/authorized_keys
            sed -i 's/#PubkeyAuthentication/PubkeyAuthentication/g' /etc/ssh/sshd_config
        fi
        ssh-keygen -A
        ssh-keygen -t rsa -C ${GITEMAIL}
        touch /hexo/sshconfig.tmp
    else
        echo "SSH config is ok!"
    fi
}

# start ssh server
startssh() {
    if [[ ! -f /hexo/setgitnpm.tmp ]]
    then
        setgitnpm
        checkdir
    fi
    if [[ ! -f /hexo/installhexo.tmp ]]
    then
        installhexo
    fi
    initsshconf
    echo "SSH server starting..."
    cat ~/.ssh/id_rsa.pub | grep ${GITEMAIL}
    /usr/sbin/sshd -D
}

startssh
