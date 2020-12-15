"""twitt_clone URL Configuration"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from tweets import urls as tweet_url
from tweets.views import home_view, tweet_list_view, tweet_create_view

urlpatterns = [
    path('', home_view),
    path('vue/', TemplateView.as_view(template_name='pages/tweets.html')),
    path('admin/', admin.site.urls),
    path('api/tweets/', include(tweet_url, namespace='tweets')),
    path('tweets/', tweet_list_view),
    path('tweet/create/', tweet_create_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
