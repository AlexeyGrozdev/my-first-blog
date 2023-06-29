from django.shortcuts import render
from django.utils import timezone
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from blog import models
from . import serializers

""" 
Импорты
1. питоновске пакеты

2. пакеты из окружения

3. остальное
"""

"""
нейминги
классы - PascalCase
переменные, методы - snake_case
константы - SNAKE_UPPER_CASE

"""

"""
__all__ = ('', )
"""

"""
typing

def w(value: str) -> list[str]:
    a: bool = True
    return value.split('.')
"""


class PostView(ModelViewSet):
    queryset = models.Post.objects
    serializer_class = serializers.PostSerializer

    def get_queryset(self):
        return super().get_queryset().filter(published_date__lte=timezone.now()).order_by('published_date')

    @action(methods=('get',), detail=False, url_path='post-list')
    def post_list(self, *args, **kwargs):
        posts = self.get_queryset()
        return render(self.request, 'blog/post_list.html', {'posts': posts})


class CommentPostView(ModelViewSet):
    queryset = models.CommentPost.objects
    serializer_class = serializers.CommentPostSerializer

    def get_queryset(self):
        return super().get_queryset().filter(post_id=self.kwargs['post_pk'])


class LikesPostView(ModelViewSet):
    queryset = models.LikePost.objects
    serializer_class = serializers.LikesPostSerializer


class LikesCommentView(ModelViewSet):
    queryset = models.LikeComment.objects
    serializer_class = serializers.LikesCommentSerializer
