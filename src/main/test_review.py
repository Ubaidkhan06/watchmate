from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .models import Platform, Review, Watchlist


class ReviewTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='example1', password='1234')
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.stream_platform = Platform.objects.create(
            name='amazonprime', description='created by amazon', website='https://amazon.com')
        self.watchlist = Watchlist.objects.create(
            title='laptop', platform=self.stream_platform, description='description')        
        self.watchlist2 = Watchlist.objects.create(
            title='title', platform=self.stream_platform, description='description')
        self.review = Review.objects.create(user=self.user, rating=5, description='good', watchlist=self.watchlist2)



    def test_review_create(self):
        data = {
            "user":self.user,
            "rating":5,
            "description":"Good Movie!!!",
            "watchlist":self.watchlist
        }
        response = self.client.post(reverse('review-create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post(reverse('review-create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_review_create_unauthenticated(self):
        data = {
            "user":self.user,
            "rating":5,
            "description":"Good Movie!!!",
            "watchlist":self.watchlist
        }
        self.client.force_authenticate(user=None)
        response = self.client.post(reverse('review-create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    
    def test_review_update(self):
        data = {
            "user":self.user,
            "rating":5,
            "description":"great movie",
            "watchlist":self.watchlist2
        }
        response = self.client.put(reverse('review-detail', args=(self.review.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_review_list(self):
        response = self.client.get(reverse('review-list', args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_review_detail(self):
        response = self.client.get(reverse('review-detail', args=(self.review.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)












