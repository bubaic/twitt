from django.conf import settings
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from tweets.models import Tweet
from .serializers import SerializeTweet, SerializeActions, SerializeTweetCreation

ALLOWED_HOSTS = settings.ALLOWED_HOSTS


'''
views below are with Django REST Framework
'''


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def tweet_create_view(request, *args, **kwargs):
    """
    DRF create view
    """
    serializer = SerializeTweetCreation(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response({}, status=400)


@api_view(['GET'])
def tweet_list_view(request, *args, **kwargs):
    """
    DRF list view
    """
    qs = Tweet.objects.all()
    serializer = SerializeTweet(qs, many=True)
    return Response(serializer.data, status=200)


@api_view(['GET'])
def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    DRF detail view
    """
    qs = Tweet.objects.filter(id=tweet_id)
    if not qs.exists():
        return Response({}, status=404)
    serializer = SerializeTweet(qs.first())
    return Response(serializer.data, status=200)


@api_view(['DELETE', 'POST'])
@permission_classes([IsAuthenticated])
def tweet_delete_view(request, tweet_id, *args, **kwargs):
    """
    DRF delete view
    """
    qs = Tweet.objects.filter(id=tweet_id)
    if not qs.exists():
        return Response({}, status=404)
    qs = qs.filter(user=request.user)
    if not qs.exists():
        return Response({
            "message": "Can't delete this tweet unless you're the owner"
        }, status=401)
    obj = qs.first()
    obj.delete()
    return Response({"message": "Tweet is deleted!"}, status=200)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def tweet_actions_view(request, *args, **kwargs):
    """
    DRF actions view
    actions: `like`, `dislike`, `retweet`
    """
    serializer = SerializeActions(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        tweet_id = data.get('id')
        actions = data.get('actions')
        content = data.get('content')
        qs = Tweet.objects.filter(id=tweet_id)

        if not qs.exists():
            return Response({}, status=404)
        obj = qs.first()
        if actions == 'like':
            obj.likes.add(request.user)
            serializer = SerializeTweet(obj)
            return Response(serializer.data, status=200)
        elif actions == 'dislike':
            obj.likes.remove(request.user)
            serializer = SerializeTweet(obj)
            return Response(serializer.data, status=200)
        elif actions == 'retweet':
            new_tweet = Tweet.objects.create(
                user=request.user,
                parent=obj,
                content=content
            )
            serializer = SerializeTweet(new_tweet)
            return Response(serializer.data, status=201)
    return Response({"message": "liked"}, status=200)


'''
views below are with pure Django
'''


def home_view(request):
    return render(request, "pages/home.html", context={}, status=200)


# def tweet_detail_view_django(req, tweet_id):
#     data = {'id': tweet_id}
#     status = 200
#
#     try:
#         obj = Tweet.objects.get(tweet_id)
#         data['content'] = obj.content
#     except:
#         data['message'] = "Not Found!"
#         status = 404
#
#     return JsonResponse(data, status=status)
#
#
# def tweet_list_view_django(req):
#     qs = Tweet.objects.all()
#     tweet_list = [x.serialize() for x in qs]
#     data = {
#         'response': tweet_list
#     }
#     return JsonResponse(data)
#
#
# def tweet_create_view_django(request, *args, **kwargs):
#     """
#     Django create view
#     """
#     user = request.user
#     form = TweetForm(request.POST or None)
#     next_url = request.POST.get('next') or None
#
#     if not request.user.is_authenticated:
#         user = None
#         if request.is_ajax():
#             return JsonResponse({}, status=401)
#         return redirect(settings.LOGIN_URL)
#
#     if form.is_valid():
#         obj = form.save(commit=False)
#         obj.user = user
#         obj.save()
#         if request.is_ajax():
#             return JsonResponse(obj.serialize(), status=201)  # 201 --> created
#         if next_url is not None and is_safe_url(next_url, ALLOWED_HOSTS):
#             return redirect(next_url)
#         form = TweetForm()
#
#     if form.errors:
#         if request.is_ajax():
#             return JsonResponse(form.errors, status=400)
#     return render(request, 'components/form.html', {'form': form})
#
