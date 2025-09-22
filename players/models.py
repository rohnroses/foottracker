from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)    
    flag = models.ImageField(upload_to='flags/', blank=True, null=True)

    def __str__(self):
        return self.name

