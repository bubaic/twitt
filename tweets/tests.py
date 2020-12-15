from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient

from .models import Tweet

User = get_user_model()


# Create your tests here.
class TweetTestCase(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='abc', password='888888')
        self.user2 = User.objects.create_user(username='cab', password='888888')
        Tweet.objects.create(content='test tweet 1', user=self.user)
        Tweet.objects.create(content='test tweet 2', user=self.user)
        Tweet.objects.create(content='test tweet 3', user=self.user2)
        self.count = Tweet.objects.all().count()

    def test_user_create(self):
        """user under tweets"""
        self.assertEqual(self.user.username, 'abc')

    def test_tweet_create(self):
        """tweet creation check"""
        tweet = Tweet.objects.create(content='test tweet 4', user=self.user)
        self.assertEqual(tweet.id, 4)
        self.assertEqual(tweet.user, self.user)

    def get_client(self):
        client = APIClient()
        client.login(username=self.user.username, password='888888')
        return client

    def test_tweet_list(self):
        c = self.get_client()
        resp = c.get('/api/tweets/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()), 3)

    def test_actions_like(self):
        c = self.get_client()
        resp = c.post('/api/tweets/action/', {'id': 1, 'actions': 'like'})
        self.assertEqual(resp.status_code, 200)
        likes = resp.json().get('likes')
        self.assertEqual(likes, 1)

    def test_actions_dislike(self):
        c = self.get_client()
        resp = c.post('/api/tweets/action/', {'id': 2, 'actions': 'like'})
        self.assertEqual(resp.status_code, 200)
        resp = c.post('/api/tweets/action/', {'id': 2, 'actions': 'dislike'})
        self.assertEqual(resp.status_code, 200)
        likes = resp.json().get('likes')
        self.assertEqual(likes, 0)

    def test_actions_retweet(self):
        c = self.get_client()
        count = self.count
        resp = c.post('/api/tweets/action/', {'id': 3, 'actions': 'retweet'})
        self.assertEqual(resp.status_code, 201)
        rt = resp.json().get('is_retweet')
        self.assertEqual(rt, 1)
        id = resp.json().get('id')
        self.assertNotEqual(3, id)
        self.assertEqual(count + 1, id)

    def test_create_view(self):
        req_data = {'content': 'test tweet 5'}
        count = self.count
        c = self.get_client()
        resp = c.post('/api/tweets/create/', req_data)
        self.assertEqual(resp.status_code, 201)
        resp_data = resp.json()
        _id = resp_data.get('id')
        self.assertEqual(count + 1, _id)

    def test_detail_view(self):
        c = self.get_client()
        resp = c.get('/api/tweets/2/')
        self.assertEqual(resp.status_code, 200)

    def test_delete_view(self):
        c = self.get_client()
        resp = c.delete('/api/tweets/2/delete/')
        self.assertEqual(resp.status_code, 200)
        resp = c.delete('/api/tweets/2/delete/')
        self.assertEqual(resp.status_code, 404)
        resp2 = c.delete('/api/tweets/3/delete/')
        self.assertEqual(resp2.status_code, 401)
        print(resp.json())
