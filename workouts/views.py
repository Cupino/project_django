from django.shortcuts import render
from .models import Workout
from django.contrib.auth.decorators import login_required

def home(request):
    workouts = Workout.objects.all()
    return render(request, 'home.html', {
        'workouts': workouts
    })

@login_required
def workout_list(request):
    workouts = Workout.objects.all()
    return render(request, "treningy.html", {
        "workouts": workouts
    })