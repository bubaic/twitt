from django.contrib import admin

from .models import Tweet, TweetLikes


# Register your models here.

class TweetLikeAdmin(admin.TabularInline):
    model = TweetLikes


class TweetAdmin(admin.ModelAdmin):
    inlines = [TweetLikeAdmin]
    list_display = ['__str__', 'user', 'created']
    search_fields = ['content', 'user__username', 'user__email']

    class Meta:
        model = Tweet


admin.site.register(Tweet, TweetAdmin)
