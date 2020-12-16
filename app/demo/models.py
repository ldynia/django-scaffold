from django.db import models


class Dummy(models.Model):
    day = models.IntegerField()
    weekday = models.CharField(max_length=16)
    month = models.CharField(max_length=16)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
