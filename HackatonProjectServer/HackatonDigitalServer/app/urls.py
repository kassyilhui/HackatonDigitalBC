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
    url(r'^login/', app.views.login, name='server_status'),
    url(r'^setup_user/', app.views.setup_user, name='server_status'),
    url(r'^search/', app.views.search_product, name='server_status'),
    url(r'^add_product/', app.views.addProduct, name='server_status'),
    url(r'^get_products/', app.views.getProducts, name='server_status'),
    url(r'^get_order/', app.views.getOrders, name='server_status'),
    url(r'^set_order/', app.views.setOrder, name='server_status'),
    url(r'^set_order_products/', app.views.setOrderProducts, name='server_status'),




]