from django.db import models

# Create your models here.

class Files(models.Model):
    name = models.CharField(max_length=200)
    hash = models.CharField(max_length=200)
    creation_date = models.DateTimeField()

