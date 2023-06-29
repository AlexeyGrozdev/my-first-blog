from django.shortcuts import render
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from blog import models
from . import serializers

# view = запросы со стороны пользователя


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

    '''
    Снять пост с публикации
    @action(methods=('get',), detail=False, url_path='post-list')
    def post_list(self, *args, **kwargs):
    '''


class CommentPostView(ModelViewSet):
    queryset = models.CommentPost.objects
    serializer_class = serializers.CommentPostSerializer

    def get_queryset(self):
        return super().get_queryset().filter(post_id=self.kwargs['post_pk'])

    @action(methods=['GET', ], detail=False, url_path='comments-list')
    def comments_list(self, *args, **kwargs):
        comments = self.get_queryset()
        return render(self.request, 'blog/view-some-data.html', {'data': comments})

    @action(methods=('delete', 'get'), detail=False, url_path='clear-comments')
    def clear_comments(self, *args, **kwargs):
        comments = self.get_queryset()
        comments.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    #!!!!!сгенерировать 1 коммент, чтобы понять post
    @action(methods=('post','get'), detail=False, url_path='')
    def generate(self, *args, **kwargs):
        post = self.kwargs['post_pk']
        username = 'admin'
        text = 'sample text'
        return

    '''
    !!!!!!!Сгенерировать комменты
    
    @action(methods=('put', 'get'), detail=False, url_path='generate-comments')
    def generate_comments(self, *args, **kwargs):
        comments = self.get_queryset()
    
    '''

    #!!!! снять пост с публикации
    @action(methods=(), detail=False, url_path='')
    def unpublish(self, *args, **kwargs):
        pass


class LikesPostView(ModelViewSet):
    queryset = models.LikePost.objects
    serializer_class = serializers.LikesPostSerializer

    def get_queryset(self):
        return super().get_queryset().filter(post_id=self.kwargs['post_pk'])

    @action(methods=('delete', 'get'), detail=False, url_path='clear-likes')
    def clear_likes(self, *args, **kwargs):
        likes = self.get_queryset()
        likes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LikesCommentView(ModelViewSet):
    queryset = models.LikeComment.objects
    serializer_class = serializers.LikesCommentSerializer

    def get_queryset(self):
        return super().get_queryset().filter(comment_id=self.kwargs['comment_pk'])

    @action(methods=('delete', 'get'), detail=False, url_path='clear-likes')
    def clear_likes(self, *args, **kwargs):
        likes = self.get_queryset()
        likes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


__all__ = ('PostView', 'CommentPostView', 'LikesPostView', 'LikesCommentView', )
