from django.db import models
from userapp.models import User

class Ride(models.Model):

    rider = models.ForeignKey(User, related_name='rides', on_delete=models.CASCADE)

    driver = models.ForeignKey(User, related_name='assigned_rides',
                               null=True, blank=True, on_delete=models.SET_NULL)
    pickup_location = models.CharField(max_length=255)

    dropoff_location = models.CharField(max_length=255)

    current_location = models.CharField(max_length=255, blank=True)

    status = models.CharField(max_length=20, choices=[
        ('requested', 'Requested'),
        ('accepted', 'Accepted'),
        ('started','Started'),
        ('completed','Completed'),
        ('cancelled','Cancelled')
    ],default='requested')

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)