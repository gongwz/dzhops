#!/usr/bin/env python
#coding:utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http.response import HttpResponse
from models import *
from django.http import *
from app01 import models

# Create your views here.
def login(request):
    ret = {'status':'用户名或者密码错误'}

    if request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        is_empty = all([username,password])
        if is_empty:

            count = UserInfo.objects.filter(username=username,password=password,).count()
            if count == 1:
                return HttpResponseRedirect('/app01/index/')
            else:
                ret['status'] = '用户名或者密码错误!'


        else:
            ret['status'] = '用户名或者密码不能为空!'

    return render_to_response('app01/login.html',ret)


def index(request):
    return render_to_response('app01/index.html')

def hostlist(request):
    ret = {'status':"",'data':None,}

    data = models.HostList.objects.all()
    ret['data'] = data
    return render_to_response('app01/hostlist.html',ret)

def addhost(request):
    ret = {'status':"",'data':None,}
    #新建主机
    if request.method == 'POST':
        ip = request.POST.get('ip',None)
        hostname = request.POST.get('hostname',None)
        minionid = request.POST.get('minionid',None)
        nocn = request.POST.get('nocn',None)
        catagorycn = request.POST.get('catagorycn',None)
        pacn = request.POST.get('pacn',None)
        dccn = request.POST.get('dccn',None)
        engineer = request.POST.get('engineer',None)
        remark = request.POST.get('remark',None)

        #验证用户输入是否为空
        is_empty = all([ip,hostname,minionid,nocn,catagorycn,pacn,dccn,engineer,remark,])
        if is_empty:
            models.HostList.objects.create(ip=ip,hostname=hostname,minionid=minionid,nocn=nocn,catagorycn=catagorycn,pacn=pacn,dccn=dccn,engineer=engineer,
remark=remark,)
        else:
            ret['status'] = '所填选项不能为空!'
    data = models.HostList.objects.all()
    ret['data'] = data
    return render_to_response('app01/addhost.html',ret)