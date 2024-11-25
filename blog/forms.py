from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    A form for creating or updating a comment model instance.
    """
    class Meta:
        model = Comment
        fields = ('body',)
