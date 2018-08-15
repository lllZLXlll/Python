from ..models import Post, Category, Tag
from django import template
from django.db.models.aggregates import Count

register = template.Library()

# 注册自定义模板标签
@register.simple_tag
def get_recent_post(num=5):
    # 获取Post中的前num条数据
    return Post.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def archives():
    # 这里 dates 方法会返回一个列表，列表中的元素为每一篇文章（Post）的创建时间，精确到月份，降序排列
    return Post.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def get_categories():
    # Count 计算分类下的文章数，其接受的参数为需要计数的模型的名称
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)