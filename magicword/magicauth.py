from django.contrib.auth.models import User, get_hexdigest
from magicword.models import MagicWord

class MagicBackend:
    
    def authenticate(self, username=None, password=None):
        username = "guest"
        try:
            magic_word = MagicWord.objects.get(password=password)
            if magic_word.enabled:
                try:
                    user = User.objects.get(username=username)
                except User.DoesNotExist:
                    user = User(username=username, password=get_hexdigest("sha1", "54L7", username))
                    user.first_name = "Guest"
                    user.last_name = "User"
                    user.is_active = True
                    user.is_staff = False
                    user.is_superuser = False
                    user.save()
                return user
        except MagicWord.DoesNotExist:
            pass
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None