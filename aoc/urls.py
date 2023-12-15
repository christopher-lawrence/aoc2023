from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('day_1/', views.day_one, name="day_one"), 
    path('day_2/', views.day_two, name="day_two"), 
    path('day_3/', views.day_three, name="day_three"), 
    path('day_4/', views.day_four, name="day_four"), 
    path('day_5/', views.day_five, name="day_five"), 
]
