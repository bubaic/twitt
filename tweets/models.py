from django.db import models


# Create your models here.

class Tweet(models.Model):
    """
    base model for tweets
    """
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='media/tweets/', verbose_name='tweet image', blank=True, null=True)
