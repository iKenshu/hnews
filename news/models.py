from django.db import models

from userprofiles.models import Profile


class New(models.Model):
    user = models.ForeignKey(Profile)
    title = models.CharField(max_length=255)
    url = models.URLField()
    vote = models.IntegerField(default=1)

    class Meta:
        ordering = ['-vote']

    def __str__(self):
        return self.title


class Comment(models.Model):
    new = models.ForeignKey(New, related_name='comments')
    author = models.ForeignKey(Profile)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
