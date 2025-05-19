from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=200)  # Use the correct max_length
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)

    def clean(self):
        if not self.title:
            raise ValidationError("Event title cannot be empty.")
        if not self.date:
            raise ValidationError("Event date is required.")

    def __str__(self):
        return self.title


class GuildLeader(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='leaders/', blank=True, null=True)  # Ensure this matches MEDIA_ROOT/leaders/

    def __str__(self):
        return self.name


class Campaign(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='campaigns/', blank=True, null=True)

    def __str__(self):
        return self.title


class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class GuildActivity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, related_name='activities')  # Updated on_delete

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="liked_reviews", blank=True)

    def __str__(self):
        return f"Review by {self.user.username} on {self.created_at}"


class VolunteerRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"VolunteerRequest({self.user.username}, {self.status})"
