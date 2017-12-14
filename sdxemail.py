# -*- coding:utf-8 -*-

"""
auth johnny 2017 12 14
sodexo smtp邮件模版

"""
import configparser
import smtpd


class sdxEmail(object):
    def __init__(self):
        cf = configparser.ConfigParser
        cf.read("service.conf")
        self._ip = cf.get('SMTP','IP')
        self._port = cf.get('SMTP','PORT')
        self._addr = cf.get('SMTP','ADDR')
        self._cc = cf.get('SMTP','ADDR')


    def mutt(self):
        pass



