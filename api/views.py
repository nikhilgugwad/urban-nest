from rest_framework import status, generics
from rest_framework.response import Response
from .models import User, PropertyListing, Booking, Message
from .serializers import UserSerializer, PropertyListingSerializer, BookingSerializer, MessageSerializer


class PropertyListingListCreate(generics.ListCreateAPIView):
    """
    List all property listings or create a new listing.
    """
    queryset = PropertyListing.objects.all()
    serializer_class = PropertyListingSerializer


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


class MessageListCreate(generics.ListCreateAPIView):
    """
    List all messages or create a new message.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
