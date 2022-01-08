from account import models
# from django_filters.rest_framework import DjangoFilterBackend, filterset
from main.models import *
from rest_framework import generics, mixins, permissions, status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework.views import APIView

from .pagination import WatchlistPagination
from .permissions import IsAdminOrReadOnly, IsReviewUserOrReadOnly
from .serializers import *
from .throttling import ReviewCreateThrottle, ReviewListThrottle


class WatchlistGV(generics.ListAPIView):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer
    pagination_class = WatchlistPagination
    # filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    # search_fields = ['title', 'platform__name']
    # filterset_fields = ['average_rating', 'total_reviews']


# ====================================================================

class UserReviewList(generics.ListAPIView):
    serializer_class = ReviewSerializer

    # def get_queryset(self):
    #     username = self.kwargs['username']
    #     return  Review.objects.filter(user__username = username)

    def get_queryset(self):
        username = self.request.query_params.get('username')
        return Review.objects.filter(user__username=username)

# =====================================================================


class WatchlistView(APIView):
    """
    View by extending the APIView class where you can acces the watchlist and and admin can also add to it 
    """
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        watchlist = Watchlist.objects.all()
        serializer = WatchlistSerializer(watchlist, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

# ==============================================================================


class WatchlistDetailView(APIView):
    """
    View by extending the APIView class
    """
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, pk):
        watchlist = get_object_or_404(Watchlist, pk=pk)
        serializer = WatchlistSerializer(watchlist)
        return Response(serializer.data)

    def put(self, request, pk):
        watchlist = get_object_or_404(Watchlist, pk=pk)
        serializer = WatchlistSerializer(watchlist, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk,):
        watchlist = get_object_or_404(Watchlist, pk=pk)
        watchlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ===============================================================================


class PlatformListView(mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
    """
    Views Using mixins
    """
    permission_classes = [IsAdminOrReadOnly]

    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# ============================================================================


class PlatformDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
    permission_classes = [IsAdminOrReadOnly]

# =============================================================================


class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]
    throttle_classes = [ReviewCreateThrottle, AnonRateThrottle]

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = Watchlist.objects.get(pk=pk)

        user = self.request.user
        qs = Review.objects.filter(
            watchlist=watchlist, user=user)

        """Check if this user has already reviewed this movie"""
        
        if qs.exists():
            raise ValidationError("You have already reviewed this movie!")

        """Checking the number of reviews and calculate the average rating to the watchlist"""

        if watchlist.total_reviews == 0:
            watchlist.average_rating = serializer.validated_data['rating']
        else:
            watchlist.average_rating = (
                watchlist.average_rating + serializer.validated_data['rating'])/2

        watchlist.total_reviews = watchlist.total_reviews + 1
        watchlist.save()

        serializer.save(watchlist=watchlist, user=user)
        return super().perform_create(serializer)

# =============================================================================


class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    throttle_classes = [ReviewListThrottle, AnonRateThrottle]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)

# =================================================================================


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewUserOrReadOnly]

# =================================================================================
