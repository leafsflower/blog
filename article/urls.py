from django.urls import path
from .views import ArticleListView,ArticleDetailView
from .views import ArticleCreateView, ArticleUpdateView, ArticleDeleteView
app_name = 'article'

urlpatterns = [
    path('article-list/', ArticleListView.as_view(), name='article_list'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('create/', ArticleCreateView.as_view(), name='article_create'),
    path('update/<int:pk>/', ArticleUpdateView.as_view(), name='article_update'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='article_delete'),

]
