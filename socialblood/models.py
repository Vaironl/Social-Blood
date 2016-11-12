from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


BLOOD_TYPES = ('A+', 'A+'),\
              ('A-', 'A-'),\
              ('B+', 'B+'),\
              ('B-', 'B-'),\
              ('AB+', 'AB+'),\
              ('AB-', 'AB-'),\
              ('O+', 'O+'),\
              ('O-', 'O-'),

class Request(models.Model):
    blood_type = models.CharField(max_length=3, choices =BLOOD_TYPES)
    create_date = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=120)
    user = models.ForeignKey('auth.User')

    def save(self, *args, **kwargs):
        super(Request, self).save(*args, **kwargs)

    def __str__(self):
        return self.blood_type
