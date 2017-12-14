# -*- coding:utf-8 -*-

import configparser
import suds
import time


class YcsSync(object):
    #ycswebservice加密文件需求。
    def __init__(self):
        cf = configparser.ConfigParser
        cf.read("service.conf")
        self._user = cf.get("YCS", "USER")
        self._pwd = cf.get("DB", "PASSWD")
        self._ip = cf.get("DB", "IPADDR")
        self._port = cf.get("DB", "PORT")
        self._sid = cf.get("DB", "SID")

    def getUid(self):
        return str(int(time.time() * 1000)) + str(int(time.clock() * 1000000))
    #生成YCS txn id .需要14位。

    def SyncSend(self, type, info):
        pass

    #根据类型发送数据


    def SyncRsponse(self,type, info):
        pass

    #根据回包处理回执。



