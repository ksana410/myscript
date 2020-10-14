# A Dockerfile for aria2

---

## 1.历史

* **2020-02-22** 测试版本

## 2.说明

> 每次在nas上安装aria2有点麻烦，那就自己写个容器吧！

本aria2镜像默认支持DHT网络，并且支持自动更新bt-tracker地址，使用rpc进行远程管理，默认管理密码为**password**

## 3.使用方法

* 拉取容器
* 注册并运行容器

docker pull ksana410/aria2
