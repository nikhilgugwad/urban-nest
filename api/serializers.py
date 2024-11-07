from rest_framework import serializers
from .models import User, PropertyListing, Booking, Message


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'date_joined']


class PropertyListingSerializer(serializers.ModelSerializer):
    """
    Serializer for PropertyListing model.
    """
    landlord = UserSerializer(read_only=True)

    class Meta:
        model = PropertyListing
        fields = ['id', 'title', 'description', 'location', 'price', 'amenities', 'landlord', 'date_posted']


class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer for Booking model.
    """
    tenant = UserSerializer(read_only=True)
    property_listing = PropertyListingSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'property_listing', 'tenant', 'date_requested', 'is_approved']


class MessageSerializer(serializers.ModelSerializer):
    """
    Serializer for Message model.
    """
    sender = UserSerializer(read_only=True)
    receiver = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'content', 'timestamp']
