import random

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from tweets.forms import TweetForm
from tweets.models import Tweet

ALLOWED_HOSTS = settings.ALLOWED_HOSTS


def home_view(request):
    return render(request, "pages/home.html", context={}, status=200)
    # return HttpResponse("it works")


def tweet_detail_view(req, tweet_id):
    data = {'id': tweet_id}
    status = 200

    try:
        obj = Tweet.objects.get(tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not Found!"
        status = 404

    return JsonResponse(data, status=status)


def tweet_list_view(req):
    qs = Tweet.objects.all()
    tweet_list = [{'id': x.id, 'content': x.content, 'likes': random.randint(0, 85558)} for x in qs]
    data = {
        'response': tweet_list
    }
    return JsonResponse(data)


def tweet_create_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    next_url = request.POST['next'] or None

    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if next_url is not None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form = TweetForm()
    return render(request, 'components/form.html', {'form': form})
