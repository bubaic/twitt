from django import forms

from .models import Tweet

MAX_CHARS = 140


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content) > MAX_CHARS: raise forms.ValidationError('This tweet exceeds max characters')
        return content
