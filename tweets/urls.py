from django.urls import path

from tweets.views import \
    tweet_detail_view, tweet_list_view,\
    tweet_create_view, tweet_delete_view, tweet_actions_view

app_name = 'tweets'

urlpatterns = [
    path('', tweet_list_view),
    path('action/', tweet_actions_view),
    path('create/', tweet_create_view),
    path('<int:tweet_id>/', tweet_detail_view),
    path('<int:tweet_id>/delete/', tweet_delete_view),
]
