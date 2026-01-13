from django.urls import path
from . views import home
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("workouts/", views.workout_list, name="workouts"), 
]

