from . import models
from django import forms

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'body', 'slug', 'banner']
        