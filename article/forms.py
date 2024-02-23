from django import forms
from .models import ArticlePost

class PostForm(forms.ModelForm):
    class Meta:
        model = ArticlePost
        fields = ('title',  'body','is_published','topic')
