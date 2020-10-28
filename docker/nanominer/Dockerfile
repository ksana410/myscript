FROM debian:latest
LABEL maintainer="ksana410 <ddxiong0410@gmail.com>"

ENV Wallet=4Lx8QAP47rCmMvwLdEMdxp7U9JJrvFCxZA9VWwPY4WuM5DmxVC5859EWATe
ENV RigName=lll
ENV Email=mail@mail.com

WORKDIR /xmr

ADD https://github.com/nanopool/nanominer/releases/download/v1.11.0/nanominer-linux-1.11.0.tar.gz /xmr
ADD defconfig.ini /xmr
ADD entrypoint.sh /xmr
RUN tar xzf nanominer-linux-1.11.0.tar.gz \
    && rm ./*.tar.gz \
    && mv nanominer* nanominer \
    && rm -f nanominer/config.ini \
    && chmod +x nanominer/nanominer \
    && chmod +x entrypoint.sh

ADD config.ini nanominer
CMD [ "entrypoint.sh" ]