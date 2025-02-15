from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class WeddingDetails(models.Model):
    bride = models.CharField(max_length=100)
    groom = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    date = models.DateField()
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()
    ceremony_time = models.TimeField()
    ceremony_venue = models.CharField(max_length=100)
    ceremony_location = models.CharField(max_length=100)
    reception_name = models.CharField(max_length=100)
    reception_location = models.CharField(max_length=100)
    reception_time = models.TimeField()
    
    def __str__(self):
        return self.bride
    
class Media(models.Model):
    image = models.ImageField(upload_to='media', blank=True, null=True)
    video = models.FileField(upload_to='media', blank=True, null=True)
    logo = models.FileField(upload_to='media', blank=True, null=True)
    slide1 = models.ImageField(upload_to='media', blank=True, null=True)
    
    
class RSVP(models.Model):
    ATTENDANCE = [
        ('yes', 'Yes, I will attend'),
        ('no', 'No, I will not attend'),
    ]
    message = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    attendance = models.CharField(max_length=100, choices=ATTENDANCE)
    guest_count = models.PositiveBigIntegerField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Message(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name