from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Travel(models.Model):
    place = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='TravelPhotos/',null=True, blank=True)
    touristGuide = models.ForeignKey('TouristGuide', on_delete=models.CASCADE, null=True, blank=True, related_name='guides')

    def __str__(self):
        return self.place or f"Travel #{self.id}"

class TouristGuide(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    surname = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name



