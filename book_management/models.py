from django.db import models
from users.models import User


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='book')
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(null = True, blank = True)
    bookImage = models.FileField(upload_to='book_images/', blank=True, null=True)


    def __str__(self):
        return self.title