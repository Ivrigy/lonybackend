"""
WSGI config for drf_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

# 1. Point Django at your settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drf_api.settings")

# 2. Monkey‑patch the default_storage proxy
from django.core.files.storage import default_storage
from cloudinary_storage.storage import MediaCloudinaryStorage

default_storage._wrapped = MediaCloudinaryStorage()

# 3. Finally load the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
