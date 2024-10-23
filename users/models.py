from django.db import models
import jwt
from datetime import datetime
from django.conf import settings


class User(models.Model):
    name = models.CharField(max_length=100,unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    creationDate = models.DateTimeField(auto_now=True)

    @property
    def is_authenticated(self):
        return True
    

    # def is_authenticated(self):
    #     """Check if the user's token is valid and not expired."""
    #     if self.accessToken and self.tokenExpiry:
    #         if datetime.now() < self.tokenExpiry:
    #             try:
    #                 jwt.decode(self.accessToken, settings.SECRET_KEY, algorithms=['HS256'])
    #                 return True
    #             except jwt.ExpiredSignatureError:
    #                 return False
    #             except jwt.InvalidTokenError:
    #                 return False
    #     return False