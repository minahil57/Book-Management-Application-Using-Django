from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(null = True, blank = True)
    bookImage = models.FileField(upload_to='book_images/', blank=True, null=True)
