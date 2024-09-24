from django.db import models


class Cats(models.Model):
    catName = models.CharField(max_length=15, unique=True)
    catAge = models.IntegerField()
    catBreed = models.CharField(max_length=50)
    catHairiness = models.CharField(max_length=15)
