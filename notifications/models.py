from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField

from account.models import User

class Search(models.Model):
    terms_en = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    websites = models.ManyToManyField("Websites")
    details = ArrayField(
        models.CharField(max_length=150),
        null=True,
        blank=True
    )

    def __str__(self):
        return self.terms_en

class Websites(models.Model):
    base_url = models.URLField()
    url = models.URLField()
    url_right = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name