=========
MagicWord
=========

MagicWord provides password-only authentication for protected pages and sites.


Installation
============

#. Configure django.contrib.auth according to the `documentation <https://docs.djangoproject.com/en/1.4/topics/auth/>`_.

#. Add `magicword` to INSTALLED_APPS in settings.py.

#. Add `magicword.backends.MagicWordBackend` to AUTHENTICATION_BACKENDS in settings.py.

#. Replace the username field in `registration/login.html` (or a custom login form) with a hidden username field with a value of 'guest'.


Protect a page
==============

Use Django's `login_required decorator <https://docs.djangoproject.com/en/dev/topics/auth/#the-login-required-decorator>`_.


Protect a site
==============

Install the MagicWord middleware::

    MIDDLEWARE_CLASSES = (
        ...
        'magicword.middleware.MagicWordMiddleware',
        ...
    )
