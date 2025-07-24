"""
WSGI config for drf_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""
import os
from django.core.wsgi import get_wsgi_application
import django.core.files.storage
from cloudinary_storage.storage import MediaCloudinaryStorage

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drf_api.settings')

django.core.files.storage.default_storage = MediaCloudinaryStorage()

application = get_wsgi_application()
