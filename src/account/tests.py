from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework import status

# Create your tests here.

class AccountsTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='example1', password='1234')

    def test_register(self):
        data = {
            'username' : 'ubaidkhan',
            'email' : 'ubaid@xyz.com',
            'password': '1234',
            'password2' : '1234'
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_login(self):
        data = {
            'username':'example1',
            'password':'1234'
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_logout(self):
        self.token = Token.objects.get(user__username='example1')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)