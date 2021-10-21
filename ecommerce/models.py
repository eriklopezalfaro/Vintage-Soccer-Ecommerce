from django.db import models

# Create your models here.
class ShoppingCart(models.Model):
    pass

class Item(models.Model):
    title = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    price = models.CharField(max_length=25)

    def __str__(self):
        return self.title