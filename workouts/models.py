from django.db import models
from django.contrib.auth.models import User

import datetime 
from django.utils import timezone

class Workout(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title 