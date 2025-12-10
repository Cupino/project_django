from django.shortcuts import render
from .models import Workout

def home(request):
    workouts = Workout.objects.all()
    return render(request, 'workouts/home.html', {
        'workouts': workouts
    })
