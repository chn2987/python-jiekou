#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017年12月6日

@author:主函数用于控制全局
'''
import requests
import huoqu_shouye
import huoqu_dingtu
import dingyou
if __name__ == "__main__":
    zhu=huoqu_shouye.leidiao()#获取探索首页
    dingt=huoqu_dingtu.get_dingtu(zhu)#获取叮途列表
    dingy=dingyou.leidiao2(zhu)#获取叮友主页
    
    
    
    
    