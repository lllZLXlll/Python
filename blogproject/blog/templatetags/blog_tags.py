from ..models import Post, Category
from django import template

register = template.Library()

# 注册自定义模板标签
@register.simple_tag
def get_recent_post(num=5):
    # 获取Post中的前num条数据
    return Post.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def archives():
    # 这里 dates 方法会返回一个列表，列表中的元素为每一篇文章（Post）的创建时间，精确到月份，降序排列
    data = Post.objects.dates('created_time', 'month', order='DESC')
    print(data)
    return data



@register.simple_tag
def get_categories():
    return Category.objects.all()