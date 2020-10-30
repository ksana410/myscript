#
# Dockerfile for Hexo
# 

FROM alpine:latest
LABEL maintainer="ksana410 <ddxiong0410@gmail.com>"
ENV PROXY=
ENV PASSWORD=password
ENV GITSITE=

RUN apk add --no-cache nodejs npm git openssh openssh-client s6 \
    && npm install npm -g \
    && npm install hexo-cli -g \
    && mkdir /hexo \
    && mkdir ~/.ssh \
    && mkdir /s6

EXPOSE 22

COPY s6/ /s6/

VOLUME [ "/hexo","/root/.ssh" ]

CMD [ "/usr/bin/s6-svscan","/s6" ]
