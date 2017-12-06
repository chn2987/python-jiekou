#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017年12月6日

@author:查看叮有主页
'''
import requests   #先导入包,这是必须的
import json
import re
class AddBook2(object):
    def __init__(self, name,phone='78787'):#默认值78787
        self.name = name
        self.phone=phone
        
    def get_phone2(self,fan):
        u'''获取叮趣首页接口(POST请求)'''
        url = 'https://services.ding-qu.com/v3/user/we/getthelist'
        data={"mu_id":"889","page":{"current":1,"rowcount":20},"access_token":""+(fan)}
        headers ={'Content-Type':'application/json'}#引用变量self.phone(拼接字符串)
        r = requests.post(url,json = data,headers = headers)
        chen=r.json()#把响应的json数据写入到chen
#         print(chen)#打印响应json数据
#         print(r.url)#返回url地址
#         print (r.status_code)#响应状态码
        print(r.text)#打印响应数据
        chen='mdq_picturepathilist' in r.text
        #断言根据响应状态码
        if r.status_code==200:
            print("刷新叮友主页-断言成功")
        else:
            print("刷新叮友主页-断言失败")
            
        if chen==True:
            print("刷新叮友主页-断言成功")
        else:
            print("刷新叮友主页-断言失败")
            
        return r.url


def leidiao2(fhui):
    Detian = AddBook2(5)#创建对象,只传一个值
    chen=Detian.get_phone2(fhui)
    
  