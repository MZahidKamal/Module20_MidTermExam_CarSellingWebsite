from django.contrib import admin
from .models import PaymentMethods_Model, Purchase_Model

# Register your models here.
admin.site.register(PaymentMethods_Model)
admin.site.register(Purchase_Model)
