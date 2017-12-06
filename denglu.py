#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017年11月20日

@author:实现叮趣登录_接口(GET请求)
'''
import requests
import json
import re

def get_denglu():
    u'''实现叮趣登录接口(GET请求)'''
    url = "https://services.ding-qu.com/v3/user/login/accountpassword?logul_longitude%5B%5D=113.357769&logul_longitude%5B%5D=23.134109&logul_precision=65.000000&mu_device=683028364449151212084245&mu_password=8a05529ec2d68a4d81b3ca6937ca2728&uservalues=18612260669"#测试的接口url
    headers = {"Content-Type":"application/json"}
    r = requests.get(url = url,headers = headers)
#     print (r.text)   #获取响应报文
#     chen=r.json()
#     print(chen)#打印响应json数据
#     print (r.status_code)#响应状态码
#     print(r.url)#返回url地址
    wei=r.text
    rr=re.findall(r"access_token\":\"(.+?)\"",wei)
    a= "" .join(rr)
    #print(self.phone)#打印全局变量
    if r.status_code==200:
        print('登录成功')
        return a
    else:
        print ('登录失败')




