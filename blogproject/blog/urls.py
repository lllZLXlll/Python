# -*- coding: utf-8 -*-

"""
路由文件

此文件作用域在blog工程范围内
blogproject 作用于整个工程
"""

from django.conf.urls import url
from . import views
from blog.feeds import AllPostsRssFeed

app_name = 'blog'
urlpatterns = [
    # 1：网址  2：处理函数  3：处理函数的别名
    url(r'^$', views.IndexView.as_view(), name='index'),

    # 博客详情，/post/1 根据id为1 查找数据中的文章
    # 以 post/ 开头，后跟一个至少一位数的数字，并且以 / 符号结尾，如 post/1/、 post/255/ 等都是符合规则的，[0-9]+ 表示一位或者多位数
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name="detail"),

    # 归档，根据年月筛选文章
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),

    # 分类，根据类别筛选文章
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name="category"),

    # 标签，根据标签筛选文章
    url(r'^tags/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name="tags"),

    # RSS订阅
    url(r'^all/rss/$', AllPostsRssFeed(), name="rss"),

    # 搜索
    # url(r'^search/$', views.search, name="search"),

]
