from rest_framework import serializers

from blog.models import Post


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

