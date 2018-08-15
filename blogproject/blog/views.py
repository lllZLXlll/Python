from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Post, Category
from comments.forms import CommentForm
import markdown
from django.views.generic import ListView, DetailView

# 首页
class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

# 文章详情
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        # 覆写 get 方法的目的是因为每当文章被访问一次，就得将文章阅读量 +1
        # get 方法返回的是一个 HttpResponse 实例
        # 之所以需要先调用父类的 get 方法，是因为只有当 get 方法被调用后，
        # 才有 self.object 属性，其值为 Post 模型实例，即被访问的文章 post
        response = super(PostDetailView, self).get(request, *args, **kwargs)

        # 将文章阅读量 +1
        # 注意 self.object 的值就是被访问的文章 post
        self.object.increase_views()

        # 视图必须返回一个 HttpResponse 对象
        return response

    def get_object(self, queryset=None):
        # 覆写 get_object 方法的目的是因为需要对 post 的 body 值进行渲染
        post = super(PostDetailView, self).get_object(queryset=None)
        # 记得在顶部引入 markdown 模块
        post.body = markdown.markdown(post.body,
                                      extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                      ])
        return post

    def get_context_data(self, **kwargs):
        # 覆写 get_context_data 的目的是因为除了将 post 传递给模板外（DetailView 已经帮我们完成），
        # 还要把评论表单、post 下的评论列表传递给模板。
        context = super(PostDetailView, self).get_context_data(**kwargs)
        # 实例化表单对象
        form = CommentForm()
        # 获取此篇文章下的所有评论
        comment_list = self.object.comment_set.all()
        context.update({
            'form': form,
            'comment_list': comment_list
        })
        return context

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


