"""
Definition of urls for HackatonDigitalServer.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^getStatus/', app.views.getStatus, name='server_status'),
]