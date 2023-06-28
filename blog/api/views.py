from rest_framework.viewsets import ModelViewSet

from blog.api.serializers import BlogSerializer
from blog.models import Post

from django.shortcuts import render
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


class BlogView(ModelViewSet):

    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    serializer_class = BlogSerializer


