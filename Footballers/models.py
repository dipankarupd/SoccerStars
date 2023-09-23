from django.db import models

# Create your models here.

class Footballer(models.Model):
    name = models.CharField(max_length=100, default = '')
    position = models.CharField(max_length=100, default = '')
    team =  models.CharField(max_length=100, default = '')


