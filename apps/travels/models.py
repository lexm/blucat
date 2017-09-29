# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..logreg.models import User

class Plan(models.Model):
    dest = models.CharField(max_length=255)
    descr = models.CharField(max_length=255)
    start = models.DateField()
    end = models.DateField()
    planned_by = models.ForeignKey('logreg.User', related_name="planned_trips")
    joined_by = models.ManyToManyField('logreg.User', related_name="joined_trips")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
