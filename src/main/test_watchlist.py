from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .models import Platform, Watchlist


class WatchlistTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='example1', password='1234')
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.stream_platform = Platform.objects.create(
            name='amazonprime', description='created by amazon', website='https://amazon.com')
        self.watchlist = Watchlist.objects.create(
            title='laptop', platform=self.stream_platform, description='description')

    def test_wacthlist_create(self):
        data = {
            "title": "Spiderman",
            "platform": self.stream_platform,
            "description": "hero movie"
        }
        response = self.client.post(reverse("platform-list"), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_watchlist_list(self):
        response = self.client.get(reverse('watchlist'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_watchlist_detail(self):
        response = self.client.get(
            reverse('watchlist-detail', args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

