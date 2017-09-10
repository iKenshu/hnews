from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class New(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    url = models.URLField()
    vote = models.IntegerField(default=1)

    class Meta:
        ordering = ['-vote']

    def __str__(self):
        return self.title

class Comment(models.Model):
    new = models.ForeignKey(New, related_name='comments')
    author = models.ForeignKey(User)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.text