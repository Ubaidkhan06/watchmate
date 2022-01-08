from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from main.models import Platform

# Create your tests here.


class StreamPlatformTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='example1', password='1234')
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.stream_platform = Platform.objects.create(
            name='amazonprime', description='created by amazon', website='https://amazon.com')
#===================================================================================================
    def test_streamplatform_create(self):
        data = {
            "name": "Netflix",
            "description": "#1 Streaming platform",
            "website": "https://netflix.com"
        }
        response = self.client.post(reverse('platform-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#===================================================================================================
    def test_platform_list(self):
        response = self.client.get(reverse('platform-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_platform_detail(self):
        response = self.client.get(
            reverse('platform-detail', args=(self.stream_platform.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
#===================================================================================================
