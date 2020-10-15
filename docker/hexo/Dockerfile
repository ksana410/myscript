#
# Dockerfile for Hexo
# 

FROM alpine:latest
LABEL maintainer="ksana410 <ddxiong0410@gmail.com>"
ENV PROXY=http://172.16.1.10:1081
ENV GITSITE=

RUN apk add --no-cache nodejs npm git openssh openssh-client s6 && \
    npm install npm -g && \
    npm install hexo-cli -g && \
    mkdir /hexo && \
    mkdir ~/.ssh && \
    mkdir /s6 && \
    npm config set proxy ${PROXY} && \
    npm config set https-proxy ${PROXY} && \
    git config --global http.proxy ${PROXY} && \
    git config --global https.proxy ${PROXY} && \
    echo 'root:password' | chpasswd && \
    echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config && \
    echo 'Port 22' >> /etc/ssh/sshd_config && \
    ssh-keygen -A

EXPOSE 22

COPY s6 /s6
VOLUME [ "/hexo","/root/.ssh" ]

CMD ["/usr/sbin/sshd","-D"]
