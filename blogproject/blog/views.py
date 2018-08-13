from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Post, Category
from comments.forms import CommentForm
import markdown
from django.views.generic import ListView

# 首页
class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

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
class ArchivesView(IndexView):
    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return super(ArchivesView, self).get_queryset().filter(
            created_time__year=year,
            created_time__month=month
        )

    # post_list = Post.objects.filter(
    #     created_time__year=year,
    #     created_time__month=month
    # )
    # return render(request, 'blog/index.html', context={'post_list': post_list})

# 分类
# CategoryView 类中指定的属性值和 IndexView 中是一模一样的，所以如果为了进一步节省代码，甚至可以直接继承 IndexView
class CategoryView(IndexView):
    # 覆写了父类的 get_queryset 方法。该方法默认获取指定模型的全部列表数据。为了获取指定分类下的文章列表数据，改变它的默认行为
    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)

    # # 根据前端传递的id查询出这一分类
    # cate = get_object_or_404(Category, pk=pk)
    # # 根据分类查询分类下所有的文章
    # post_list = Post.objects.filter(category=cate)
    # return render(request, 'blog/index.html', context={'post_list': post_list})


