from rest_framework import serializers

from rideing.models import Ride

class Rideserializer(serializers.ModelField):

    class Meta:

        model = Ride

        fields = "__all__"