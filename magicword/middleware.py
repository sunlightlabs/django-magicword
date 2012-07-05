from django.contrib.auth.views import redirect_to_login
from django.core.urlresolvers import reverse


class MagicWordMiddleware(object):

    def process_request(self, request):

        if not request.user.is_authenticated():

            login_url = reverse('login')

            if login_url != request.path:
                return redirect_to_login(request.path)
