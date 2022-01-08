from rest_framework.pagination import CursorPagination

# class WatchlistPagination(PageNumberPagination):
#     page_size = 3
#     page_size_query_param = 'page_size'
#     max_page_size = 5

class WatchlistPagination(CursorPagination):
    page_size = 3
    ordering = ['-created_at']
