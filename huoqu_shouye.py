#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017年9月21日

@author:主要实现_获取首页(POST请求)
'''
#__________________________________使用面向对象方式接口(获取叮趣首页)____________________________________________________________

import requests   #先导入包,这是必须的
import json
import re
import denglu

class AddBook(object):
    def __init__(self, name,phone='78787'):#默认值78787
        self.name = name
        self.phone=phone
        
    def get_phone(self,fan):
        u'''获取叮趣首页接口(POST请求)'''
        while self.name<10:
            #print(self.name)
            url = 'https://services.ding-qu.com/v3/user/tansuo/getlist'
            data={"mu_id":889,"mdq_picturecoordinate":[113.357725,23.134038],"page":{"current":1,"rowcount":50,"srotfield":[]}}
            headers ={'Content-Type':'application/json','access_token':''+(fan)}#引用变量self.phone(拼接字符串)
            r = requests.post(url,json = data,headers = headers)
            chen=r.json()#把响应的json数据写入到chen
#             print(chen)#打印响应json数据
#             print(r.url)#返回url地址
#             print (r.status_code)#响应状态码
            print(r.text)#打印响应数据
            a=r.text
            chen='操作成功' in a
            if chen==True:
                print("获取首页列表-断言成功")
                return fan
            else:
                print("获取首页列表-断言失败")
            return r.url


def leidiao():
    Detian = AddBook(5)#创建对象,只传一个值
    Meng = AddBook(5, '18210413002')#实例化类，或为类创建对象
    fhui=denglu.get_denglu()#调用登录
    chen=Meng.get_phone(fhui)
    return chen
    #print (Detian.get_phone())#通过Detian对象调用(调用首页接口)
    #print (Meng.get_phone())#通过Meng对象调用
    
