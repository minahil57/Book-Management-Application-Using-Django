
from django.contrib import admin
from django.urls import path,include

from users import views
from book_management import views
from review_management import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', include('users.urls')),
    path('book/', include('book_management.urls')),
    path('review/', include('review_management.urls')),
]
