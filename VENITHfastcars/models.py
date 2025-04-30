from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=260)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class offer(models.Model):
    code = models.CharField(max_length=15)
    description = models.CharField(max_length=260)
    discount = models.FloatField()

    

