from __future__ import unicode_literals

# Create your views here.





import json
from django.shortcuts import render


# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

# 引入我们创建的表单类
from DjangoProjectPay import settings
from .forms import AddForm

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def index(request):
    return render(request, 'index.html')


def catinfo(request):
    if request.method == "POST":
        f1 = request.FILES['pic1']
        fname = '%s/pic/%s' % (settings.MEDIA_ROOT, f1.name)
        print(fname)
        with open(fname, 'wb') as pic:
            for c in f1.chunks():
                pic.write(c)
        return HttpResponse("ok")
    else:
        return HttpResponse("error")


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a + b))

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

def addRedi(request,a,b):
    return  HttpResponseRedirect(reverse('add2', args=(a, b)))



def uploadpic(request):
    return render(request,'update_pic.html')


def home(request):
    List = ['django学习', '渲染Json到模板']
    Dict = {'site': '123', 'author': 'zqj'}
    return render(request, 'learn/home.html', {
        'List': json.dumps(List),
        'Dict': json.dumps(Dict)
    })

