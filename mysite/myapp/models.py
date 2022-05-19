from django.db import models
from django.forms import CharField, FloatField, IntegerField
from django.contrib.auth.models import User
# Create your models here.


class Food(models.Model):
    name = models.CharField(max_length=100)
    carbs = models.FloatField()
    protien = models.FloatField()
    fats = models.FloatField()
    calorie = models.IntegerField()

    def __str__(self) -> str:
        return self.name

class Consume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_cosume = models.ForeignKey(Food, on_delete=models.CASCADE)
    
