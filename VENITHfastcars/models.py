from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=260)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    description = models.TextField(blank=True)


class Offer(models.Model):
    code = models.CharField(max_length=15)
    description = models.CharField(max_length=260)
    discount = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.code
    
    @property
    def discount_percentage(self):
        return self.discount * 100


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"
