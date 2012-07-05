import uuid

from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from magicword.models import MagicWord

MAGICAUTH_USERNAME = getattr(settings, 'MAGICAUTH_USERNAME', 'guest')
MAGICAUTH_FIRST_NAME = getattr(settings, 'MAGICAUTH_FIRST_NAME', 'Guest')
MAGICAUTH_LAST_NAME = getattr(settings, 'MAGICAUTH_LAST_NAME', 'User')


class MagicWordBackend(object):

    def authenticate(self, username=None, password=None):

        username = MAGICAUTH_USERNAME

        if MagicWord.objects.filter(password=password, is_enabled=True).exists():

            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:

                password = make_password(uuid.uuid4().hex)

                user = User(username=username, password=password)
                user.first_name = MAGICAUTH_FIRST_NAME
                user.last_name = MAGICAUTH_LAST_NAME
                user.is_active = True
                user.is_staff = False
                user.is_superuser = False
                user.save()

            return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
