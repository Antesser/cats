from django.db import models
from django.contrib.auth.models import User


class Cats(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    catName = models.CharField(max_length=15, unique=True)
    catAge = models.IntegerField()
    catBreed = models.CharField(max_length=50)
    catHairiness = models.CharField(max_length=15)
