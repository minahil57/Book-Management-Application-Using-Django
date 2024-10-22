from django.urls import path, include
from .views import AddBookView, GetBookList, DeleteBookView, UpdateBookView, GetBookView
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()

routers.register(r'add_book', AddBookView, basename='add_book')
routers.register(r'book_list',GetBookList , basename='book_list')
routers.register(r'update_book', UpdateBookView, basename='update_book')
routers.register(r'delete_book', DeleteBookView , basename='delete_book')
routers.register(r'get_book', GetBookView , basename='get_book')

urlpatterns = [
    path('', include(routers.urls)),  # Include the router's URLs
]

print("router: ", routers.urls)