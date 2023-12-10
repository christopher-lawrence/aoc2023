from django.urls import path

from . import views

urlpatterns = [
    path('day_one/', views.day_one, name="day_one"), 
    path('day_two/', views.day_two, name="day_two"), 
    path('day_three/', views.day_three, name="day_three"), 
]
