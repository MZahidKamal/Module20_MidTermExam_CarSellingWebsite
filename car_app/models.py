from django.db import models


# Create your models here.
class Brand_Model(models.Model):
    name = models.CharField(max_length=20)              # Audi / Mercedes / BMW / Toyota / Ford etc
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name


class Car_Model(models.Model):
    manufacturer = models.ForeignKey(Brand_Model, on_delete=models.CASCADE)
    model = models.CharField(max_length=100, unique=True)
    capacity = models.CharField(max_length=50)          # 2.2 L Diesel 190 bhp etc.
    shift = models.CharField(max_length=20)             # Automatic / Manual / Combined
    fuel = models.CharField(max_length=20)              # Petrol / Diesel / Gas / Electricity / Plug-in hybrid
    top_speed = models.IntegerField()                   # 127 Km/h
    price = models.PositiveIntegerField()               # 42800 Euro
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='car_app/media/uploads/', null=True, blank=True)

    def __str__(self):
        return f"{self.manufacturer} -- {self.model}"


class Comments_Model(models.Model):
    car = models.ForeignKey(Car_Model, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, unique=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} commented on {self.created_at}'
