from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile


# 定义一个自定义的 UserAdmin
class UserProfileAdmin(UserAdmin):
    # 添加 avatar 到 fieldsets 中，这样在 admin 界面中就可以编辑它了
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('avatar',)}),
    )

    # 如果你也想在创建用户时能够添加头像，可以更新 add_fieldsets
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('avatar',)}),
    )


# 注册你的模型和自定义的 UserAdmin
admin.site.register(UserProfile, UserProfileAdmin)
