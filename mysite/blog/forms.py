from django import forms
from .models import Post, Authorisation


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


class EnterForm(forms.ModelForm):
    class Meta:
        model = Authorisation
        fields = ('login', 'password', 'password')
