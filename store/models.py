from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name