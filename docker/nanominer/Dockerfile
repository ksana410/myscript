FROM debian:latest
LABEL maintainer="ksana410 <ddxiong0410@gmail.com>"

ENV Wallet=
ENV RigName=
ENV Email=
ARG XMR_VERSION="1.11.0"
ARG TAG=master

WORKDIR /xmr

ADD https://github.com/nanopool/nanominer/releases/download/v${XMR_VERSION}/nanominer-linux-${XMR_VERSION}.tar.gz /xmr
ADD defconfig.ini /xmr
ADD entrypoint.sh /xmr
RUN tar xzf nanominer-linux-1.11.0.tar.gz \
    && rm ./*.tar.gz \
    && mv nanominer* nanominer \
    && rm -f nanominer/config.ini \
    && chmod +x nanominer/nanominer \
    && chmod +x entrypoint.sh

ADD config.ini nanominer
CMD [ "./entrypoint.sh" ]