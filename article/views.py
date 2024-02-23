
from django.urls import reverse_lazy
from django.views.generic import ListView
from .models import ArticlePost
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

import markdown

class ArticleListView(ListView):
    model = ArticlePost
    template_name = 'article/list.html'  # 假设你的模板位于这个路径

    # 可选：如果你想自定义查询集（比如只显示已发布的文章）
    def get_queryset(self):
        return ArticlePost.objects.filter(is_published=True)




class ArticleDetailView(DetailView):
    model = ArticlePost
    template_name = 'article/detail.html'  # 假设你的模板位于这个路径
    def get_context_data(self, **kwargs):
        # 调用父类的get_context_data来获取上下文
        context = super().get_context_data(**kwargs)
        # 获取当前文章对象
        article = context['object']
        md = markdown.Markdown(
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ])
        article.body = md.convert(article.body)
        context['article'] = article
        # 将目录信息添加到上下文中
        context['toc'] = md.toc
        return context



from django.views.generic.edit import CreateView
from .models import ArticlePost
from .forms import PostForm

class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = ArticlePost
    form_class = PostForm
    template_name = 'article/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # 设置作者为当前登录用户
        return super().form_valid(form)

    def get_success_url(self):
        # 删除成功后重定向到文章列表页
        return reverse_lazy('article:article_list')

    # 设置登录重定向URL
    login_url = '/userprofile/login/'




from django.views.generic.edit import UpdateView

class ArticleUpdateView(LoginRequiredMixin,UpdateView):
    model = ArticlePost
    template_name = 'article/update.html'
    fields = ['title', 'body']  # 允许更新的字段


    def get_queryset(self):
        """只允许作者编辑自己的文章"""
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)

    def get_success_url(self):
        # 更新成功后重定向到文章详情页，这里使用了对象的 `pk` 来构造URL
        return reverse_lazy('article:article_detail', kwargs={'pk': self.object.pk})

    # 设置登录重定向URL
    login_url = '/userprofile/login/'


from django.views.generic.edit import DeleteView


class ArticleDeleteView(LoginRequiredMixin,DeleteView):
    model = ArticlePost

    def get_queryset(self):
        """只允许作者删除自己的文章"""
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)

    def get_success_url(self):
        # 删除成功后重定向到文章列表页
        return reverse_lazy('article:article_list')
    # 设置登录重定向URL
    login_url = '/userprofile/login/'
