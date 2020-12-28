from django.forms import ModelForm
from .models import Image, Comment

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['description', 'path']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']