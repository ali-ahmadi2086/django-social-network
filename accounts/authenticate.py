from django.contrib.auth.models import User
from django.contrib.auth.backends import BaseBackend


class EmailBackend(BaseBackend):

    def authenticate(self, request, **kwargs):
        try:
            user = User.objects.get(email=kwargs['username'])
            if user.check_password(kwargs['password']):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None