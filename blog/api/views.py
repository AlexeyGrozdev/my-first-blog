from rest_framework.viewsets import ModelViewSet

from blog.api.serializers import BlogSerializer
from blog.models import Post

from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})


class BlogView(ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = BlogSerializer


