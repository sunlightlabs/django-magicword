from django.contrib.auth.views import redirect_to_login


class MagicWordMiddleware(object):

    def process_request(self, request):

        if not request.user.is_authenticated():
            return redirect_to_login(request.path)
