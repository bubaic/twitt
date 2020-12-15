from django import forms
from django.conf import settings

from .models import Tweet

MAX_CHARS = settings.TWEET_MAX_LENGTH


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content) > MAX_CHARS:
            raise forms.ValidationError('This tweet exceeds 140 characters')
        return content
