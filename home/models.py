from django.db import models

class Food(models.Model):
    food_name = models.CharField(max_length=200)
    food_price = models.IntegerField(default=0)
class Baverage(models.Model):
    baverage_name = models.CharField(max_length=200)
    baverage_price = models.IntegerField(default=0)