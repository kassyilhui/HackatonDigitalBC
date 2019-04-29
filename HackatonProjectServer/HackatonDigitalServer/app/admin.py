# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from app.models import product,user,inventory,inventory_products

admin.site.register(product)
admin.site.register(user)
admin.site.register(inventory)
admin.site.register(inventory_products)