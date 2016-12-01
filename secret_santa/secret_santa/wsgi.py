"""
WSGI config for secret_santa project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
# Added from Whitenoise page
from whitenoise import WhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "secret_santa.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
# Added from Whitenoise page
application = WhiteNoise(application, root='/static')