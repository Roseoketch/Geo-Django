# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import name, location, pub_date

# Register your models here.
admin.site.register(name)
admin.site.register(location)
admin.site.register(pub_date)
