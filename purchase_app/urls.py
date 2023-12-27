from django.urls import path
from .views import car_purchase

urlpatterns = [
    path('<int:car_id>/', car_purchase, name='car_purchase'),
]

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# from .views import Car_Profile
#
# urlpatterns = [
#     path('profile/<int:id>/', Car_Profile.as_view(), name='car_profile'),
# ]
