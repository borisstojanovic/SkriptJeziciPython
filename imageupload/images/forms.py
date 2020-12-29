from django.forms import ModelForm
import django.forms as f
from .models import Image


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'description', 'path']