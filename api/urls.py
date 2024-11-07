from django.urls import path
from . import views

urlpatterns = [
    # Property Listing Endpoints
    path('properties/', views.PropertyListingListCreate.as_view(), name='property-list-create'),
    path('properties/<int:pk>/', views.PropertyListingRetrieveUpdateDestroy.as_view(), name='property-retrieve-update-destroy'),
    
    # Booking Endpoints
    path('bookings/', views.BookingListCreate.as_view(), name='booking-list-create'),
    
    # Message Endpoints
    path('messages/', views.MessageListCreate.as_view(), name='message-list-create'),
]
