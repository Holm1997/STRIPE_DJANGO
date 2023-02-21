from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.name
    
    def display_price(self):
        return "{0:.2f}".format(self.price / 100)
