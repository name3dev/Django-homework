from django.db import models

# Create your models here.


class Order(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    product = models.CharField(max_length=50)
    quantity = models.IntegerField()

    delivery = models.CharField(max_length=20)
    address = models.CharField(max_length=255, blank=True)

    total_price = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
