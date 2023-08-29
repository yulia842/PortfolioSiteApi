from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.id},{self.name}, {self.description}, {self.price}"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"cart id:{self.id} ,product id : {self.product}, {self.user}, quantity : {self.quantity}"