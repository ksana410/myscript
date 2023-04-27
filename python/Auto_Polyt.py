# -*- coding: utf-8 -*-

# 基于协程来运行程序

import requests
from pprint import pprint
import time
import json
import re
import userdata
import 


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
        self.retry_count = 3
        
    # # 建立get操作，如果失败则重试三次，三次重试失败后终止函数
    # def _get(self, url: str):
    #     retry_count = 3
    #     try:
    #         response = self.session.get(url)
    #         response.raise_for_status()
    #         if response.json()['success']:
    #             return response.json()
    #         else:
    #             raise Exception(response.json()['errors'])
    #     except Exception as e:
    #         print(e)
    #         if retry_count > 0:
    #             retry_count -= 1
    #             return self._get(url)
    #         else:
    #             print("重试失败，程序终止！")
    #             exit()
    
    # # 建立post操作，三次请求失败则退出程序
    # def _post(self, url: str, json_data: dict):
    #     retry_count = 3
    #     try:
    #         response = self.session.post(url, json = json_data)
    #         response.raise_for_status()
    #         if response.json()['success']:
    #             return response.json()
    #         else:
    #             raise Exception(response.json()['errors'])
    #     except Exception as e:
    #         print(e)
    #         if retry_count > 0:
    #             retry_count -= 1
    #             return self._post(url, json_data)
    #         else:
    #             print("重试失败，程序终止！")
    #             exit()
    
    # # 建立delete操作，三次重试失败即退出
    # def _delete(self, url: str, json_data: dict):
    #     retry_count = 3
    #     try:
    #         response = self.session.delete(url, json = json_data)
    #         response.raise_for_status()
    #         if response.json()['success']:
    #             return response.json()
    #         else:
    #             raise Exception(response.json()['errors'])
    #     except Exception as e:
    #         print(e)
    #         if retry_count > 0:
    #             retry_count -= 1
    #             return self._delete(url, json_data)
    #         else:
    #             print("重试失败，程序终止！")
    #             exit()
    
    # 合并 get, post, delete 功能，使用一个方法实现三种功能
    def _req(self, method: str, url: str, json_data: dict = {}):
        try:
            if method == 'get':
                rep = self.session.get(url)
            elif method == 'post':
                rep = self.session.post(url, json = json_data)
            elif method == 'delete':
                rep = self.session.delete(url, json = json_data)
            else:
                print('method error')
                exit()
            rep.raise_for_status()
            if rep.json()['success']:
                return rep.json()
            else:
                raise Exception(rep.json()['errors'])
        except  Exception as e:
            print(e)
            exit()

                
    # 关闭连接
    def _close(self):
        self.session.close()
        
    # 获取演出时间，票价
    def get_time_price(self):
        data = self._req('post', self.url + 'good/search-products-data', {'keyword': self.keyword})
        if data['success']:
            records = data['data']['records']
            productId = None
            for record in records:
                if self.city in record['cityName']:
                    productId = record['productId']
                    break
            if productId:
                productDetail = self._req('get', self.url + 'good/shows/' + productId) 
                DetailList = productDetail['data']['showInfoDetailList']
                show_dict = dict(zip(range(len(DetailList)), [j['showTime'] for j in DetailList]))
                show_detail = {}
                # 获取演出时间和票价-ID相关的信息
                for k, v in show_dict.items():
                    show_detail[v] = { str(i['price']): i['priceId'] for i in DetailList[k]['ticketPriceList'] if i['ticketCount'] != 0}
                return show_detail
                

    # 选定演出的场次和票价
    def select_time_price(self):
        pass
    
    # 管理观演人信息，增加，选择或者删除
    def manage_viewers(self, operate = 'list'):
        viewers_list = self._req('get', self.url + 'member/viewers')['data'] 
        viewers_dict = dict(zip([str(i) for i in range(len(viewers_list))], [ i['name'] for i in viewers_list]))
        if operate == 'select':
            pprint(viewers_dict)
            # 选择观演人，逐个选择，直到按下回车结束，如果输入的序号不存在，则输出重试信息
            viewers_selected = []
            viewers_can_sel = list(viewers_dict.keys())
            while 1:
                viewers_index = input(f'请在如下列表中选择观演人序号{viewers_can_sel}，按回车结束')
                if viewers_index not in viewers_dict.keys() and viewers_index != '':
                    print(f'{viewers_index}不存在，请重新输入')
                    continue
                elif viewers_index not in viewers_selected and viewers_index != '':
                    viewers_selected.append(viewers_index)
                    viewers_can_sel.remove(viewers_index)
                    if len(viewers_can_sel) == 0:
                        break
                    continue
                elif viewers_index in viewers_selected:
                    print(f'{viewers_index}已被选择')
                    continue
                else:
                    break
            return [viewers_list[int(index)]['id'] for index in viewers_selected]
        # 添加观演人的操作，基于身份证号码进行匹配，如果从未添加过就添加进去
        elif operate == 'add':
            id = (input('请输入观演人身份证号：')).upper()
            # 身份证正则匹配，特意按照日期格式进行了匹配优化
            if re.match(r'[1-9]/d{5}[12][09][0-9]{2}[12][0-9]{3}[01][0-9][03]/d{4}[0-9X]', id):
                for viewer in viewers_list:
                    if viewer['credentialsCode'] == id:
                        print(f'{viewer["name"]}已被添加')
                        return
                name = input('请输入观演人姓名：')
                add_viewer = self._req('post', self.url + 'member/viewers', {"credentialsCode": id, "cardTypeEnum": "ID_CERT","name": name, "id": "", "top": 0})
                if add_viewer['success']:
                    print(f'{name}已添加')
            else:
                print('身份证号格式错误!\n')
                self.manage_viewers('add')
        # 删除观演人，选择删除
        elif operate == 'delete':
            pprint(viewers_dict)
            viewers_selected = self.manage_viewers('select')
            pass
        else:
            return [ i['name'] + ':' + i['credentialsCode'] for i in viewers_list ]
        
    # 使用短信验证码进行登录，需要绕过 cf.aliyun.com 的滑动验证码
    def login(self, phone):
        pass

    # 运行
    def run(self):
        pass

if __name__ == '__main__':
    start = polytAuto("白夜行", "无锡")
    pprint(start.get_time_price())