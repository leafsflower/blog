from django.db import models
from django.utils import timezone
from userprofile.models import UserProfile
# 博客文章数据模型
from userprofile.models import UserProfile  # 确保从正确的位置导入UserProfile

from django.db import models
from django.utils import timezone
# 假设UserProfile已经被定义在 somewhere
from mdeditor.fields import MDTextField

class Topic(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name




class ArticlePost(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = MDTextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_DEFAULT, default=1)  # 假设ID为1的Topic是'未归档'
    # 新增是否已发布字段
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title



