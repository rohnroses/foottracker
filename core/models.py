from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)    
    def __str__(self):
        return self.name
    
class League(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='leagues')
    season = models.CharField(max_length=9, blank=True)

    def __str__(self):
        return f"{self.name} ({self.season})" if self.season else self.name
    
class Club(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True, related_name='clubs')
    league = models.ForeignKey(League, on_delete=models.SET_NULL, null=True, blank=True, related_name='clubs')
    def __str__(self):
        return self.name

class Player(models.Model):
    POSITION_CHOICES = [
        ('RW', 'Right Winger'),
        ('LW', 'Left Winger'),
        ('ST', 'Striker'),
        ('CF', 'Center Forward'),
        ('LB', 'Left Back'),
        ('RB', 'Right Back'),
        ('CB', 'Center Back'),
        ('CDM', 'Defensive Midfielder'),
        ('CM', 'Central Midfielder'),
        ('CAM', 'Attacking Midfielder'),
        ('GK', 'Goalkeeper'),
    ]
    fullname = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True)
    position = models.CharField(max_length=5, choices=POSITION_CHOICES) 
    league = models.ForeignKey(League, on_delete=models.SET_NULL, null=True)
    transfer_value = models.IntegerField(null=True, blank=True, validators=[
        MinValueValidator(0), 
        MaxValueValidator(200_000_000)
    ],
    help_text="Трансферная стоимость в евро")

    def __str__(self):
        return self.fullname
    
