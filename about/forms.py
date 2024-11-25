from django import forms
from .models import CollaborateRequest


class CollaborateForm(forms.ModelForm):
    """
    A form for creating or updating a collaboration request model instance.
    """
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')
