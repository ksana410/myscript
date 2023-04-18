# -*- coding: utf-8 -*-

import requests
from pprint import pprint
import time
import json
import re
import userdata


cookie = userdata.cookie
authorization = userdata.authorization
header = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36 Edg/112.0.1722.34',
    'Referer': 'https://m.polyt.cn/',
    'Authorization': authorization,
    'Content-Type': 'application/json',
    'Channel': 'plat_h5',
    'Connection': 'keep-alive',
    'Cookie': cookie
}

# 对象化编程
# 执行流程如下
# 1. 要求用户输入演出名，所处城市，工具会基于上述两个输入确定具体的演出项目
# 2. 脚本应具有两种模式，抢购模式，普通模式，抢购模式只需要确认演出名，城市，观演人即可，默认每场都抢购
# 3. 此时对象自动将获取到的演出时间，票价，观演人, 此时可以添加观演人，最终存储用户所选，需要注意，由于实名制的要求，购票数量对应观演人数量，故指定观演人即可
# 4. 之后软件将自动运行，直到抢购到为止
class polytAuto:
    def __init__(self, keyword: str, city: str):
        self.keyword = keyword
        self.city = city
        self.url = 'https://m.polyt.cn/platform-backend/'
        self.session = requests.session()
        self.session.headers.update(header)
        
    # 建立get操作，如果失败则重试三次，三次重试失败后终止函数
    def _get(self, url: str):
        retry_count = 3
        try:
            response = self.session.get(url)
            response.raise_for_status()
            if response.json()['success']:
                return response.json()
            else:
                print(response.json()['errors'])
                return None
        except Exception as e:
            print(e)
            if retry_count > 0:
                retry_count -= 1
                return self._get(url)
            else:
                print("重试失败，程序终止！")
                exit()
    
    # 建立post操作，三次请求失败则退出程序
    def _post(self, url: str, json_data: dict):
        retry_count = 3
        try:
            response = self.session.post(url, json = json_data)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(e)
            if retry_count > 0:
                retry_count -= 1
                return self._post(url, json_data)
            else:
                print("重试失败，程序终止！")
                exit()
    
    # 建立delete操作，三次重试失败即退出
    def _delete(self, url: str, json_data: dict):
        retry_count = 3
        try:
            response = self.session.delete(url, json = json_data)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(e)
            if retry_count > 0:
                retry_count -= 1
                return self._delete(url, json_data)
            else:
                print("重试失败，程序终止！")
                exit()
                
    # 关闭连接
    def _close(self):
        self.session.close()
        
    # 获取演出时间，票价
    def get_time_price(self):
        data = self._post(self.url + 'good/search-products-data', {'keyword': self.keyword})
        if data['success']:
            records = data['data']['records']
            productId = None
            for record in records:
                if self.city in record['cityName']:
                    productId = record['productId']
                    break
            if productId:
                productDetail = self._get(self.url + 'good/shows/' + productId)
                DetailList = productDetail['data']['showInfoDetailList']
                pprint(DetailList)
    
    # 管理观演人信息，增加，选择或者删除
    def manage_viewers(self, operate = 'select'):
        viewers_list = self._get(self.url + 'member/viewers')['data']
        viewers_dict = dict(zip(range(len(viewers_list)), [ i['name'] for i in viewers_list]))
        if operate == 'select':
            pprint(viewers_dict)
            # 选择观演人，逐个选择，直到按下回车结束，如果输入的序号不存在，则输出重试信息
            while 1:

        
    # 使用短信验证码进行登录，需要绕过 cf.aliyun.com 的滑动验证码
    def login(self, phone):
        pass

if __name__ == '__main__':
    start = polytAuto("白夜行", "无锡")
    pprint(start.get_time_price())
    pprint(start.manage_viewers())