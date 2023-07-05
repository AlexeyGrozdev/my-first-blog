from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class CommentPost(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='comments')
    username = models.CharField(verbose_name='Логин', max_length=32)
    text = models.CharField(verbose_name='Текст', max_length=256)

    def __str__(self):
        return self.username+": "+self.text


class LikePost(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='likes_post')
    username = models.CharField(verbose_name='Логин', max_length=32)


class LikeComment(models.Model):
    comment = models.ForeignKey(to=CommentPost, on_delete=models.CASCADE, related_name='likes_comment')
    username = models.CharField(verbose_name='Логин', max_length=32)


__all__ = ('Post', 'CommentPost', 'LikePost', 'LikeComment', )
