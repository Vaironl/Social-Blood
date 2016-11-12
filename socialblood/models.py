from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator

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

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed.")
    phone_number = models.CharField(max_length=16, validators=[phone_regex])

    def save(self, *args, **kwargs):
        super(Request, self).save(*args, **kwargs)

    def __str__(self):
        return self.blood_type
