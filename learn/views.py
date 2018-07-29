from __future__ import unicode_literals

# Create your views here.





import json
from django.shortcuts import render


# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

# 引入我们创建的表单类
from .forms import AddForm

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def index(request):
    return render(request, 'index.html')


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






def home(request):
    List = ['自强学堂', '渲染Json到模板']
    Dict = {'site': '自强学堂', 'author': '涂伟忠'}
    return render(request, 'home.html', {
        'List': json.dumps(List),
        'Dict': json.dumps(Dict)
    })