from django import forms

from .models import *


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'url', 'email', 'body']
        labels = {
            'name': '请输入名字',
            'url': '输入主页',
            'email': '输入邮箱',
            'body': '输入正文'
        }
        widgets={
             'body':forms.Textarea
        }
