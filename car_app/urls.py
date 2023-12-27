from django.urls import path
# from .views import car_profile
#
# urlpatterns = [
#     path('profile/', car_profile, name='car_profile'),
# ]

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from .views import Car_Profile

urlpatterns = [
    path('profile/<int:id>/', Car_Profile.as_view(), name='car_profile'),
]
