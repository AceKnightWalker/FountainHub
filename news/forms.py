from django import forms
from django.forms import ModelForm
from .models import Comment, Article


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)

class PostForm(ModelForm):
    class Meta:
        model = Article
        fields = ['picture', 'headline', 'content']