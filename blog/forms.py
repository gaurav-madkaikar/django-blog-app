# Create forms for the database models

from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    # Meta class will inform what model will be referred to
    class Meta:
        model = Post
        fields = ('title', 'text')

