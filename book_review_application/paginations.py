# paginations.py

from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 5  # Number of objects per page
    page_size_query_param = 'page_size'  # Allow the client to set page size in query
    max_page_size = 100  # Maximum limit on page size
