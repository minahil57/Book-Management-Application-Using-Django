from django.db import models
from users.models import User
from book_management.models import Book


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    rating = models.FloatField()
    review = models.TextField()
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
