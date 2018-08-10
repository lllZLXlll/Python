# -*- coding: utf-8 -*-

"""
路由文件

此文件作用域在blog工程范围内
blogproject 作用于整个工程
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    # 1：网址  2：处理函数  3：处理函数的别名
    url(r'^$', views.index, name='index')
]
