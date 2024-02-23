from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    # 添加一个头像字段
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
