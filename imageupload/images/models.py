import os

from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver

class Image(models.Model):
    title = models.CharField(max_length=64, default='')
    path = models.ImageField(upload_to='upload\\')
    num_views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    description = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    def is_liked(self):
        return self.likes > self.dislikes

@receiver(models.signals.post_delete, sender=Image)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.path:
        if os.path.isfile(instance.path.path):
            os.remove(instance.path.path)

@receiver(models.signals.pre_save, sender=Image)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = Image.objects.get(pk=instance.pk).path
    except Image.DoesNotExist:
        return False

    new_file = instance.path.path
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)