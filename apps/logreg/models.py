# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=255)
    alias = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
