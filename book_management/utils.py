from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import User  # Assuming this is where your User model is
from .utils import authenticate_user_from_token

class CustomJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # Extract the token from the 'Authorization' header
        auth_header = request.headers.get('Authorization')

        if not auth_header or not auth_header.startswith('Bearer '):
            return None  # No authentication attempt if there's no token

        token = auth_header.split(' ')[1]  # Extract the token part

        # Use your custom token validation function
        is_authenticated, message = authenticate_user_from_token(token)

        if not is_authenticated:
            raise AuthenticationFailed(message)

        # If authentication is successful, return the user and token
        try:
            user = User.objects.get(email=message)  # Assuming your function returns email on success
            return (user, None)  # 'None' for the auth token part since it's already handled
        except User.DoesNotExist:
            raise AuthenticationFailed('User does not exist')

