from django.contrib import admin
from django.db import models

from main.models import Platform, Review, Watchlist

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['rating', 'watchlist', 'user', 'description']


class WatchlistAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'platform']
    readonly_fields  = ['total_reviews', 'average_rating']


class WatchlistTabularInline(admin.TabularInline):
    model = Watchlist
    fields = ['title', 'description', 'is_active']


class PlatformAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'website']
    inlines = [WatchlistTabularInline]


admin.site.register(Watchlist, WatchlistAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(Review, ReviewAdmin)
