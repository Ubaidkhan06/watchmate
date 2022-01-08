from os import read
from rest_framework import serializers
from main.models import Platform, Review, Watchlist


# Create your seriazliers here

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        exclude = ['created_at', 'watchlist', 'updated_at']

#==========================================================

class WatchlistSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True)
    platform = serializers.CharField(source = 'platform.name')
    class Meta:
        model = Watchlist
        fields = '__all__'

#==========================================================


class PlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchlistSerializer(many=True, read_only=True)
    class Meta:
        model = Platform
        fields = '__all__'

#==========================================================

