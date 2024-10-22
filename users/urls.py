from django.urls import path, include
from .views import LoginView, RegisterView
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()

routers.register(r'login', LoginView, basename='login')
routers.register(r'register', RegisterView, basename='register')

urlpatterns = [
    path('', include(routers.urls)),  # Include the router's URLs
]

print("router: ", routers.urls)

