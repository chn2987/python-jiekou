#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017年12月2日

@author:刷新叮途列表(GET请求)
'''
import requests
import json
import re

def get_dingtu(tok):
    u'''刷新叮途列表'''
    url = "https://services.ding-qu.com/v3/dingtu/getthe?access_token="+str(tok)+"&mu_id=889" 
    headers = {"Content-Type":"application/json"}
    r = requests.get(url = url,headers = headers)
    print (r.text)   #获取响应报文
#     print(r.json())#打印响应json数据
#     print (r.status_code)#响应状态码
#     print(r.url)#返回url地址
    #print(self.phone)#打印全局变量
    if r.status_code==200:
        print('刷新叮途成功')
    else:
        print ('刷新叮途失败')
