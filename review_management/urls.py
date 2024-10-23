from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import AddReviewView,GetSpecificBookReviews,EditReviewView,DeleteReviewView


routers = DefaultRouter()

routers.register(r'add_review', AddReviewView, basename='add_review')
routers.register(r'review_list',GetSpecificBookReviews , basename='book_review_list')
routers.register(r'update_review', EditReviewView, basename='update_book')
routers.register(r'delete_review', DeleteReviewView , basename='delete_review')
# routers.register(r'get_review', GetBookView , basename='get_book')

urlpatterns = [
    path('', include(routers.urls)),  # Include the router's URLs
]