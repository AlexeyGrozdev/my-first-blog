from rest_framework import serializers

from blog import models


class PostSerializer(serializers.ModelSerializer):
    comment_list = serializers.SerializerMethodField(label='Список комментариев')
    comment_count = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()

    class Meta:
        model = models.Post
        fields = '__all__'

    def validate_author(self, value):
        return

    @staticmethod
    def get_comment_list(instance):
        return [x.text for x in instance.comments.all()]

    @staticmethod
    def get_comment_count(instance) -> int:
        return instance.comments.count()

    @staticmethod
    def get_likes(instance):
        return instance.likes_post.count()


class CommentPostSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    class Meta:
        model = models.CommentPost
        fields = '__all__'

    @staticmethod
    def get_likes(instance):
        return instance.likes_comment.count()


class LikesPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LikePost
        fields = '__all__'


class LikesCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LikeComment
        fields = '__all__'
