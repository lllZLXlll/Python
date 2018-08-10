from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    # render 函数，根据传入参数构造HttpResponse
    return render(
        request,
        'blog/index.html',
        context={
            'title': '我的博客主页',
            'welcome': '欢迎访问我的博客首页'

        }

    )