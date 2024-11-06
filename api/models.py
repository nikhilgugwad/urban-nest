from django.db import models

class User(models.Model):
    """
    Model representing a user of the application (tenant or landlord).
    """
    ROLE_CHOICES = [
        ('tenant', 'Tenant'),
        ('landlord', 'Landlord'),
    ]
    
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class PropertyListing(models.Model):
    """
    Model representing a property listing.
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amenities = models.TextField(blank=True)
    landlord = models.ForeignKey(User, on_delete=models.CASCADE, related_name="properties")
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Booking(models.Model):
    """
    Model representing a booking request for a property.
    """
    property_listing = models.ForeignKey(PropertyListing, on_delete=models.CASCADE)
    tenant = models.ForeignKey(User, on_delete=models.CASCADE)
    date_requested = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking by {self.tenant} for {self.property_listing}"


class Message(models.Model):
    """
    Model for messages between landlord and tenant.
    """
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender} to {self.receiver} at {self.timestamp}"
