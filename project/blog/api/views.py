from random import randint, choice
from string import ascii_letters

from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from . import serializers
from .. import models

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
        return super().get_queryset().filter()

    @action(methods=('get',), detail=False, url_path='list')
    def post_list(self, *args, **kwargs):
        posts = self.get_queryset().filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(self.request, 'blog/post_list.html', {'posts': posts})

    @action(methods=('put', 'get'), detail=True, url_path='unpublish')
    def unpublish(self, *args, **kwargs):
        post = self.get_queryset().filter(id=self.kwargs['pk']).first()
        published_date = None;
        post.published_date = published_date
        post.save()
        return Response(status=status.HTTP_202_ACCEPTED)

    @action(methods=('put', 'get'), detail=True, url_path='republish')
    def republish(self, *args, **kwargs):
        post = self.get_queryset().filter(id=self.kwargs['pk']).first()
        published_date = timezone.now()
        post.published_date = published_date
        post.save()
        return Response(status=status.HTTP_202_ACCEPTED)


class CommentPostView(ModelViewSet):
    queryset = models.CommentPost.objects
    serializer_class = serializers.CommentPostSerializer

    def get_queryset(self):
        return super().get_queryset().filter(post_id=self.kwargs['post_pk'])

    @action(methods=['GET', ], detail=True, url_path='view')
    def view(self, *args, **kwargs):
        comment = self.get_queryset().filter(id=self.kwargs['pk'])
        for i in comment:
            data = str(i)
        return JsonResponse(data, safe=False)

    @action(methods=['GET', ], detail=False, url_path='list')
    def comments_list(self, *args, **kwargs):
        comments = self.get_queryset()
        return render(self.request, 'blog/view-some-data.html', {'data': comments})

    @action(methods=('delete', 'get'), detail=False, url_path='clear')
    def clear_comments(self, *args, **kwargs):
        comments = self.get_queryset()
        comments.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=('post', 'get'), detail=False, url_path='generate')
    def generate_comments(self, *args, **kwargs):
        post = models.Post.objects.filter(pk=self.kwargs['post_pk']).first()
        comments = []
        for _ in range(30):
            username = ""
            text = ""
            for _ in range(randint(6, 18)):
                username += choice(ascii_letters)
            for _ in range(randint(18, 54)):
                text += choice(ascii_letters)
            comments += [str(models.CommentPost.objects.create(post=post, username=username, text=text))]
        return Response(data={'comments': comments})


class LikesPostView(ModelViewSet):
    queryset = models.LikePost.objects
    serializer_class = serializers.LikesPostSerializer

    def get_queryset(self):
        return super().get_queryset().filter(post_id=self.kwargs['post_pk'])

    @action(methods=('post', 'get'), detail=False, url_path='generate')
    def generate_likes(self, *args, **kwargs):
        post = models.Post.objects.filter(pk=self.kwargs['post_pk']).first()
        likes = []
        for _ in range(7):
            username = ""
            for _ in range(randint(6, 18)):
                username += choice(ascii_letters)
            likes += [str(models.LikePost.objects.create(post=post, username=username))]
        return Response(status=status.HTTP_201_CREATED)

    @action(methods=('delete', 'get'), detail=False, url_path='clear')
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


__all__ = ('PostView', 'CommentPostView', 'LikesPostView', 'LikesCommentView',)
