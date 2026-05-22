from django.db import models

class FoodOrder(models.Model):
    Order_ID = models.IntegerField(primary_key=True)
    CustomerName = models.CharField(max_length=50)
    RestaurantName = models.CharField(max_length=50)
    FoodItem = models.CharField(max_length=100)
    Quantity = models.IntegerField()
    Price = models.FloatField()
    DeliveryAddress = models.CharField(max_length=200)
    OrderStatus = models.CharField(max_length=30)

    def __str__(self):
        return self.CustomerName