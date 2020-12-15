from django.conf import settings
from rest_framework import serializers

from .models import Tweet

TWEET_MAX_LENGTH = settings.TWEET_MAX_LENGTH
ACTIONS = settings.TWEET_ACTION_OPTS


class SerializeActions(serializers.Serializer):
    id = serializers.IntegerField()
    actions = serializers.CharField()
    content = serializers.CharField(allow_blank=True, required=False)

    @staticmethod
    def validate_actions(val):
        val = val.lower().strip()
        if val not in ACTIONS:
            raise serializers.ValidationError('Not a valid action!')
        return val


class SerializeTweetCreation(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Tweet
        fields = ['id', 'content', 'likes']

    @staticmethod
    def get_likes(obj):
        return obj.likes.count()

    @staticmethod
    def validate_content(value):
        if len(value) > TWEET_MAX_LENGTH:
            raise serializers.ValidationError('This tweet exceeds 140 characters')
        return value


class SerializeTweet(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    parent = SerializeTweetCreation(read_only=True)

    class Meta:
        model = Tweet
        fields = ['id', 'content', 'likes', 'is_retweet', 'parent']

    @staticmethod
    def get_likes(obj):
        return obj.likes.count()