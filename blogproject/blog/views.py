from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

def index(request):
    # render 函数，根据传入参数构造HttpResponse
    # return render(
    #     request,
    #     'blog/index1.html',
    #     context={
    #         'title': '我的博客主页',
    #         'welcome': '欢迎访问我的博客首页'
    #
    #     }
    #
    # )

    # 查询所有文章数据，按照创建时间降序排列 -表示降序
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={
        'post_list': post_list,
        'title': '我的博客主页',
        'welcome': '欢迎访问我的博客首页'
    })

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', context={'post': post})