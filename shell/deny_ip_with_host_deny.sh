#!/bin/bash
# Copyright 2020/01/04
# A Script For Deny Ip With Host.deny

# 读取日志，将连续超过5次ssh验证失败的IP筛选出来并生成临时文件
cat /var/log/auth.log |awk '/preauth/{print $(NF-3)}'|grep [0-9]|sort|uniq -c|awk '{if($1 > 5) print $2}' > /tmp/hosts.txt

# 逐条读取临时文件并比对host.deny中的内容，如果没有就加上
for i in `cat /tmp/hosts.txt`
do
    if [ `grep -c $i /etc/hosts.deny` -eq 0 ];then
            echo "sshd:$i:deny" >> /etc/hosts.deny
    fi
done