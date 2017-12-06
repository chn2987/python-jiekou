#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017年9月21日

@author:主要实现首页列表接口请求
'''
#——————————————————————获取叮趣首页接口————————————————————————————————

'''
import requests   #先导入包,这是必须的
import json
import re
a=1
while a<1000:
    url = 'https://services.ding-qu.com/v3/user/tansuo/getlist'       
    #data = {'isWeb':'true','loginName':'18612260669','loginPass':'432705'}
    data={"mu_id":889,"mdq_picturecoordinate":[113.357725,23.134038],"page":{"current":1,"rowcount":50,"srotfield":[]}}
    headers ={'Content-Type':'application/json','access_token':'bdb4610f23f3d93de2ba9468ae85cd28'}
    #注意这里的数据传入要json格式，不然报错 
    r = requests.post(url,json = data,headers = headers)
    chen=r.json()
    #print(chen)
    wei= chen["errmsg"]#获取'errmsg'的内容
    #print(wei)
    #print(r.text) #请求url，获得返回的数据信息
    #print(r.url)#返回url地址
    #print(r.status_code)#返回状态码
    #print (r.text.encode("utf-8"))
    a+=1
    if a>=999:
        print (a)
    elif "成功" in wei:#判断返回数据的状态
        print ('返回断言-ture')
    else:
        print ("false")
        
'''        
#__________________________________使用面向对象方式接口(获取叮趣首页)____________________________________________________________

import requests   #先导入包,这是必须的
import json
import re
class AddBook(object):
    def __init__(self, name,phone='78787'):#默认值78787
        self.name = name
        self.phone=phone
    def get_denglu(self):
        u'''实现叮趣登录接口(GET请求)'''
        url = "https://services.ding-qu.com/v3/user/login/accountpassword?logul_longitude%5B%5D=113.357769&logul_longitude%5B%5D=23.134109&logul_precision=65.000000&mu_device=683028364449151212084245&mu_password=8a05529ec2d68a4d81b3ca6937ca2728&uservalues=18612260669"#测试的接口url
        headers = {"Content-Type":"application/json"}
        r = requests.get(url = url,headers = headers)
        print (r.text)   #获取响应报文
        #print (r.status_code)#响应状态码
        wei=r.text
        rr=re.findall(r"access_token\":\"(.+?)\"",wei)
        a= "" .join(rr)
        self.phone=a
        #print(self.phone)#打印全局变量
        if r.status_code==200:
            print('登录成功')
        else:
            print ('登录失败')

    def get_phone(self):
        u'''获取叮趣首页接口(POST请求)'''
        while self.name<10:
            #print(self.name)
            url = 'https://services.ding-qu.com/v3/user/tansuo/getlist'
            data={"mu_id":889,"mdq_picturecoordinate":[113.357725,23.134038],"page":{"current":1,"rowcount":50,"srotfield":[]}}
            headers ={'Content-Type':'application/json','access_token':''+(self.phone)}#引用变量self.phone(拼接字符串)
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
            else:
                print("获取首页列表-断言失败")
            return r.url


# 调用
if __name__ == "__main__":
    Detian = AddBook(5)#创建对象,只传一个值
    Meng = AddBook(5, '18210413002')#实例化类，或为类创建对象
    chen1=Meng.get_denglu()#调用登录接口
    #print(chen1)
    Meng.get_phone()
    #print (Detian.get_phone())#通过Detian对象调用(调用首页接口)
    #print (Meng.get_phone())#通过Meng对象调用
    
