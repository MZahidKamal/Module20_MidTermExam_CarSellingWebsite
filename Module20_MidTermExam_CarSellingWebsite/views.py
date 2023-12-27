from django.shortcuts import render
from car_app.models import Brand_Model, Car_Model


def base(request):
    return render(request, 'base.html')


def home(request, brand_slug=None):
    brands = Brand_Model.objects.all().order_by('name')
    if brand_slug:
        brand = Brand_Model.objects.get(slug=brand_slug)
        cars = Car_Model.objects.filter(manufacturer=brand)
    else:
        cars = Car_Model.objects.all()
    context = {
        'brands': brands,
        'cars': cars,
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
