from rest_framework.viewsets import ModelViewSet

from rest_framework.decorators import action

from rest_framework.response import Response

from rideing.models import Ride

from rideing.serializers import Rideserializer

from rest_framework.permissions import IsAuthenticated

from userapp.models import User

from django.test import TestCase



class RideView(ModelViewSet):

    queryset = Ride.objects.all()

    serializer_class = Rideserializer

    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        serializer.save(rider=self.request.user)

    @action(detail=True, methods=['patch'])

    def update_status(self, request, pk=None):

        ride = self.get_object()

        ride.status = request.data.get('status')

        ride.save()
        
        return Response({'status': 'Ride status updated'})


    @action(detail=True, methods=['post'])

    def accept(self, request, pk=None):

        ride = self.get_object()

        if request.user.is_driver:

            ride.driver = request.user

            ride.status = 'accepted'

            ride.save()

            return Response({'message': 'Ride accepted'})
        
        return Response({'error': 'Only drivers can accept rides'}, status=403)

    @action(detail=True, methods=['patch'])

    def update_location(self, request, pk=None):

        ride = self.get_object()

        ride.current_location = request.data.get('current_location')

        ride.save()

        return Response({'message': 'Location updated'})
    
    def driver_match(ride):

        driver = User.objects.filter(is_driver=True).first()

        ride.driver = driver

        ride.status = 'accepted'
        
        ride.save()


class RideTest(TestCase):

    def test_ride_creation(self):

        rider = User.objects.create_user(username='user1', password='abc')

        ride = Ride.objects.create(

            rider=rider,

            pickup_location='P',

            dropoff_location='D'
        )
        self.assertEqual(ride.status, 'requested')
