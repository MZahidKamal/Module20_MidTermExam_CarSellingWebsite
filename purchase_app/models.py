from django.db import models
from django.contrib.auth.models import User
from car_app.models import Car_Model


# Create your models here.
class PaymentMethods_Model(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Purchase_Model(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car_Model, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.PositiveIntegerField(null=True, blank=True)
    payment_type = models.ForeignKey(PaymentMethods_Model, on_delete=models.SET_NULL, null=True)
    buy_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return f"{self.user.username} - {self.quantity}"
        return f"Customer: {self.user.first_name} {self.user.last_name},    Car: {self.car.manufacturer} {self.car.model},  Quantity: {self.quantity}, Date: {self.buy_date.date()}."
