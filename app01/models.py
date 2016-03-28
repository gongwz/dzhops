#!/usr/bin/env python
#coding:utf-8
from django.db import models

# Create your models here.

'''
资产管理用户表和资产表的设计
'''
class UserType(models.Model):
    name = models.CharField(max_length=50, blank=True, verbose_name=u'用户类型')   
    
class UserInfo(models.Model):
    username = models.CharField(max_length=50, blank=True, verbose_name=u'用户名')
    password = models.CharField(max_length=50, blank=True, verbose_name=u'密码')
    #email = models.CharField(max_length=50, blank=True, verbose_name=u'邮箱')
    user_type = models.ForeignKey('UserType')   


class HostList(models.Model):
    ip = models.CharField(max_length=15,  blank=True,verbose_name=u'IP地址')
    hostname = models.CharField(max_length=30, verbose_name=u'主机名')
    minionid = models.CharField(max_length=60, verbose_name=u'MinionID')
    nocn = models.CharField(max_length=30, verbose_name=u'运营商全称')
    catagorycn = models.CharField(max_length=30, blank=True, verbose_name=u'类别')
    pacn = models.CharField(max_length=30, verbose_name=u'地区全称')
    dccn = models.CharField(max_length=30, blank=True, verbose_name=u'机房全称')
    engineer = models.CharField(max_length=30, blank=True, verbose_name=u'维护人员')
    #macaddr = models.CharField(max_length=20,  blank=True,verbose_name=u'MAC地址')
    #zsourceip = models.CharField(max_length=30,  blank=True,verbose_name=u'主行情源')
    #bsourceip = models.CharField(max_length=30,  blank=True,verbose_name=u'备行情源')
    #dccn = models.ForeignKey(dataCenter, related_name='datacenter_hostlist')
    #licdate = models.CharField(max_length=30,  blank=True,verbose_name=u'授权日期')
    #licstatus = models.CharField(max_length=30, blank=True, verbose_name=u'授权状态')
    #engineer = models.ForeignKey(dzhuser, related_name='dzhuser_hostlist')
    #idip = models.CharField(max_length=15,  blank=True,verbose_name=u'MinionID中的IP地址')
    #ipsame = models.CharField(max_length=10,  blank=True,verbose_name=u'IP地址一致性')
    remark = models.TextField(max_length=200, blank=True, verbose_name=u'备注')