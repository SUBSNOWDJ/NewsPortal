from django import forms
from django.contrib.auth.models import Group

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'type', 'title', 'text']
