from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    column = models.IntegerField()

