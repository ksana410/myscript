# A docker image for edit hexo website

> The Dockerfile can build a ssh server with hexo

---

## Version

v0.1

## Base image

apline:latest

## Variable Description

|Variables|Default|Description|
|:--:|:--:|:--|
|PORXY||The http proxy|
|PASSWORD|password|The default ssh password|
|TAG||git branch|
|GITSITE||github url|
|GITUSER||git user|
|GITEMAIL||git email|

## Hostory

* **2021.01.18** First working version