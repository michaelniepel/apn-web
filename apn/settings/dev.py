from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-p$ev$2yixji1i*ag98r6tt77j)!a+qpv8=v)k$g_zu0rqpvlmv"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass


INSTALLED_APPS += ["django_browser_reload"]


MIDDLEWARE += ["django_browser_reload.middleware.BrowserReloadMiddleware"]