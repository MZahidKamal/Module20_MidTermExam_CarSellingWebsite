from django.contrib import admin
from .models import Car_Model, Brand_Model, Comments_Model


# Register your models here.
class Brand_Model_Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')

admin.site.register(Brand_Model, Brand_Model_Admin)
admin.site.register(Car_Model)
admin.site.register(Comments_Model)
