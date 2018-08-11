# -*- coding: utf-8 -*-

"""
路由文件

此文件作用域在blog工程范围内
blogproject 作用于整个工程
"""

from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    # 1：网址  2：处理函数  3：处理函数的别名
    url(r'^$', views.index, name='index'),

    # 博客详情，/post/1 根据id为1 查找数据中的文章
    # 以 post/ 开头，后跟一个至少一位数的数字，并且以 / 符号结尾，如 post/1/、 post/255/ 等都是符合规则的，[0-9]+ 表示一位或者多位数
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name="detail"),
]
