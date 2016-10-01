from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Request(models.Model):
    blood_type = models.CharField(max_length=4)
    create_date = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=120)

    def save(self, *args, **kwargs):
        super(Request, self).save(*args, **kwargs)

    def __str__(self):
        return self.blood_type
