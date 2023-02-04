# Nanominer for Docker

## 1.版本

nanominer-v3.7.6

## 2.说明

配置xmr挖坑的自动守护程序太麻烦（主要还是太懒），使用docker的方式不仅部署简单，而且还能自动重启进程，实在是方便！

> 如果不设置钱包地址，那么它将自动使用默认的钱包地址（本人的）

## 3.变量说明

|变量名|默认值|备注|
|:----:|:----:|:----:|
|Wallet||挖矿的钱包地址，默认为空|
|RigName||给矿机设置的名字，可以随意，当然如果你想比较好的区分的话还是起个有意义的名字|
|Email||结算时所需要用到的邮箱地址|
|Proxy||http代理（可选）|

## 4.使用方法

### 拉取镜像

docker pull ksana410/nanominer

### 运行

docker run -d --name=nanominer --restart=always -e Wallet=钱包地址 -e RigName=主机名 -e Email=邮箱地址 -e Proxy=http代理 ksana410/nanominer
