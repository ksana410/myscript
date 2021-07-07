FROM debian:latest
LABEL maintainer="ksana410 <ddxiong0410@gmail.com>"

ENV Wallet=
ENV RigName=
ENV Email=


WORKDIR /xmr

RUN apt-get update \
    && apt-get install -y wget \
    && DOWN_URL = wget -qO- -t1 -T2 "https://api.github.com/repos/nanopool/nanominer/releases/latest" |grep browser_download_url |grep linux |grep -v cuda |awk -F " " '{print $2}'
ADD ${DOWN_URL} /xmr
ADD defconfig.ini /xmr
ADD entrypoint.sh /xmr
RUN tar xzf *.tar.gz \
    && rm ./*.tar.gz \
    && apt-get autoremove -y wget \
    && apt-get autoclean \
    && mv nanominer* nanominer \
    && rm -f nanominer/*.ini \
    && chmod +x nanominer/nanominer \
    && chmod +x entrypoint.sh

ADD config.ini nanominer
CMD [ "./entrypoint.sh" ]