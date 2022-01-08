from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Platform(models.Model):
    """ 
    Streaming platform on which watchlist/movies are hosted. OnetoMany relationship with watchlist model
    """
    name = models.CharField(max_length=155)
    description = models.CharField(max_length=155)
    website = models.URLField(max_length=155)

    def __str__(self):
        return self.name


class Watchlist(models.Model):
    """
    Watchlist contains all type of content eg. Movies, TVshows, Podcast etc.
    """
    title = models .CharField(max_length=155)
    platform = models.ForeignKey(
        Platform, on_delete=models.CASCADE, related_name='watchlist')
    description = models.CharField(max_length=155)
    total_reviews = models.PositiveIntegerField(default=0)
    average_rating = models.FloatField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    """
    Review contains details of review added to the watchlist and in one to many relationship with watchlist
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=155)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    watchlist = models.ForeignKey(
        Watchlist, on_delete=models.CASCADE, related_name='reviews')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.rating)
