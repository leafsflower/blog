
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

class UserLoginView(LoginView):
    template_name = 'userprofile/login.html'  # 指定你的登录模板路径
    redirect_authenticated_user = True  # 如果用户已认证，则重定向
    def get_success_url(self):
        return reverse_lazy('article:article_list')




class UserLogoutView(LogoutView):
    next_page = reverse_lazy('article:article_list')
