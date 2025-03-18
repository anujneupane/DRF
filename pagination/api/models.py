from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
 