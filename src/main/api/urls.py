from django.urls import path
from main.api.views import (PlatformDetailView, PlatformListView,
                            ReviewCreateView, ReviewDetailView, ReviewListView,
                            UserReviewList, WatchlistDetailView, WatchlistGV,
                            WatchlistView)

urlpatterns = [

    # urls for watchlist
    path('watchlist/', WatchlistView.as_view(), name='watchlist'),
    path("watchlist/<int:pk>/", WatchlistDetailView.as_view(),name="watchlist-detail"),
    path('reviews/', UserReviewList.as_view(), name='user-review-detail'),
    path( 'list/', WatchlistGV.as_view(), name='list-view'),

    # urls for Streamingplatform
    path("platform/", PlatformListView.as_view(), name="platform-list"),
    path("platform/<int:pk>/", PlatformDetailView.as_view(), name="platform-detail"),

    # urls for reviews
    path("<int:pk>/review-create/",ReviewCreateView.as_view(), name='review-create'),
    path("<int:pk>/review/", ReviewListView.as_view(), name='review-list'),
    path("review/<int:pk>/", ReviewDetailView.as_view(), name='review-detail'),


]
