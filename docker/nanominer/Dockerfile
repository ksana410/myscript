FROM debian:latest
LABEL maintainer="ksana410 <ddxiong0410@gmail.com>"

ENV Wallet=47LyN11A63Ng1PrXMuxWb5GrVaxNDJtjifC8dLx8QAP47rCmMvwLdEMdxp7U9JJrvFCxZA9VWwPY4WuM5DmxVC5859EWATe
ENV RigName=lll
ENV Email=zoufeng4@gmail.com

WORKDIR /xmr

ADD https://github.com/nanopool/nanominer/releases/download/v1.11.0/nanominer-linux-1.11.0.tar.gz /xmr
RUN tar xzf nanominer-linux-1.11.0.tar.gz \
    && rm ./*.tar.gz \
    && mv nanominer-linux-1.11 nanominer \
    && rm -f nanominer/config.ini \
    && chmod +x nanominer/nanominer

ADD config.ini nanominer

CMD [ "/xmr/nanominer/nanominer" ]