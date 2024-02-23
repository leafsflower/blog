from django.contrib import admin
from .models import ArticlePost,Topic
from mdeditor.widgets import MDEditorWidget
from django.db import models
# 定义一个简单的 ArticlePostAdmin 管理类
class ArticlePostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created', 'updated')  # 在列表页显示的字段
    search_fields = ('title', 'body')  # 添加搜索框，可以通过标题和内容搜索
    list_filter = ('created', 'author')  # 添加过滤器，可以通过创建时间和作者过滤
    date_hierarchy = 'created'  # 添加时间层次结构导航条
    ordering = ('-created',)  # 默认的排序方式
    formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget}
    }



# 注册你的模型和管理类
admin.site.register(Topic)


admin.site.register(ArticlePost, ArticlePostAdmin)
