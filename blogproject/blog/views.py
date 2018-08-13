from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Post, Category
from comments.forms import CommentForm
import markdown

# 首页
def index(request):
    # 查询所有文章数据，按照创建时间降序排列 -表示降序
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', context={'post_list': post_list})

# 文章详情
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # 记得在顶部引入 markdown 模块
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    # 实例化表单对象
    form = CommentForm()

    # 获取此篇文章下的所有评论
    comment_list = post.comment_set.all()

    # 阅读量+1
    post.increase_views()

    context = {
        'post': post,
        'form': form,
        'comment_list': comment_list,
    }

    return render(request, 'blog/detail.html', context=context)

# 归档
def archives(request, year, month):
    post_list = Post.objects.filter(
        created_time__year=year,
        created_time__month=month
    )
    return render(request, 'blog/index.html', context={'post_list': post_list})

# 分类
def category(request, pk):
    # 根据前端传递的id查询出这一分类
    cate = get_object_or_404(Category, pk=pk)
    # 根据分类查询分类下所有的文章
    post_list = Post.objects.filter(category=cate)
    return render(request, 'blog/index.html', context={'post_list': post_list})


