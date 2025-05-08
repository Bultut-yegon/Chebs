from django import forms
from .models import Post, Activity


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['caption', 'image']

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['content', 'image']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'cols': 80, 'placeholder': 'share what is happening'}),
        }