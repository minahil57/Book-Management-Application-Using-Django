import jwt
import time

from django.conf import settings
from rest_framework import authentication, exceptions
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from .models import User


def generate_jwt_token(useremail):
    payload = {
        'Email': useremail
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token
 

class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = authentication.get_authorization_header(request).decode('utf-8')
        if not auth_header or not auth_header.startswith('Bearer '):
            return None
        # print(auth_header)
        try:
            token = auth_header.split(' ')[1]
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed('Invalid token.')
        try:
            user = User.objects.filter(email=payload['Email']).first()
            # print(user.Type)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('User not found.')
        return (user, None)











