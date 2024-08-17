from django.db import models

class StaticData(models.Model):
    message = models.CharField(max_length=255)
    numbers = models.JSONField()