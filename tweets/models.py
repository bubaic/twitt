import random

from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


# Create your models here.

class TweetLikes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey('Tweet', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class Tweet(models.Model):
    """
    base model for tweets
    """
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, verbose_name='retweets')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='tweet_user', blank=True, through=TweetLikes)
    image = models.FileField(upload_to='media/tweets/', verbose_name='tweet image', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.id) + '_' + str(self.content)

    @property
    def is_retweet(self):
        return self.parent is not None

    def serialize(self):
        """
        Django way of serializing data without DRF
        """
        return {
            'id': self.id,
            'content': self.content,
            'likes': random.randint(0, 200),
            'created': self.created
        }
