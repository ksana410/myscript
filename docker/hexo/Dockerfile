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

<<<<<<< HEAD
EXPOSE 2200
=======
ADD start.sh /
RUN chmod +x /start.sh

EXPOSE 22
>>>>>>> 75cb150a2c48294dc1092c454576e314158aa484

VOLUME [ "/hexo","/root/.ssh" ]

ENTRYPOINT [ "/start.sh" ]
CMD []
