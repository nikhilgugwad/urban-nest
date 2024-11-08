from rest_framework import status, generics
from rest_framework.response import Response
from .models import User, PropertyListing, Booking, Message
from .serializers import UserSerializer, PropertyListingSerializer, BookingSerializer, MessageSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsLandlord, IsTenant


class PropertyListingListCreate(generics.ListCreateAPIView):
    """
    List all property listings or create a new listing.
    """
    queryset = PropertyListing.objects.all()
    serializer_class = PropertyListingSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            # Only landlords can create a property listing
            self.permission_classes = [IsAuthenticated, IsLandlord]
        else:
            # All authenticated users can view property listings
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions


class PropertyListingRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a property listing.
    """
    queryset = PropertyListing.objects.all()
    serializer_class = PropertyListingSerializer


class BookingListCreate(generics.ListCreateAPIView):
    """
    List all bookings or create a new booking.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated, IsTenant]

    def perform_create(self, serializer):
        # Set the tenant automatically as the current user when creating a booking
        serializer.save(tenant=self.request.user)


class MessageListCreate(generics.ListCreateAPIView):
    """
    List all messages or create a new message.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
