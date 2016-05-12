from django.db import models

# Create your models here.
class Calcu(models.Model):
    n = models.CharField(max_length=10)
