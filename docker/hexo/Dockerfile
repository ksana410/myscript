#
# Dockerfile for SSH Server with Hexo
# 

FROM alpine:latest
LABEL maintainer="ksana410 <ddxiong0410@gmail.com>"
ENV PROXY=
ENV PASSWORD=password
ENV GITSITE=
ENV TAG=master

RUN apk add --no-cache nodejs npm git openssh openssh-client \
    && npm install npm -g \
    && npm install hexo-cli -g \
    && mkdir /hexo \
    && mkdir ~/.ssh

EXPOSE 2200

VOLUME [ "/hexo","/root/.ssh" ]

CMD [ "/usr/bin/s6-svscan","/s6" ]
