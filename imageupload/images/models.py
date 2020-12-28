from django.db import models

class Image(models.Model):
    path = models.URLField(max_length=200, default='')
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    description = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

    def is_liked(self):
        return self.likes > self.dislikes

class Comment(models.Model):
    content = models.CharField(max_length=64)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def is_liked(self):
        return self.likes > self.dislikes
