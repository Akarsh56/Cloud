# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Shop,Category,Product,Media

admin.site.register(Shop)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Media)

