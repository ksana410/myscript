# A docker image for edit hexo website

> The Dockerfile can build a ssh server with hexo

---

## Version

v0.3

## Base image

apline:latest

## Variable Description

|Variables|Default|Description|
|:---|:---:|:---|
|PORXY||The http proxy|
|PASSWORD|password|The default ssh password|
|TAG||git branch|
|GITSITE||github url|
|GITUSER||git user|
|GITEMAIL||git email|

## Hostory

* **2021.01.18** First working version
* **2021.07.09** Trigger test
* **2021.12.21** change directory to /hexo/data
