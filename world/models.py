# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class shop(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    pub_date = models.DateTimeField(auto_now_add=True)

    def__str__(self):
        return self.name
