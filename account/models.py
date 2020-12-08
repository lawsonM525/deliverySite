from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    balance = models.FloatField()
    hostel = models.CharField(max_length=255)
    room = models.IntegerField()
