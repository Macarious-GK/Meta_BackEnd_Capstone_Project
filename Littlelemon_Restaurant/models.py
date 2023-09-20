from django.db import models

# Create your models here.
class Booking(models.Model):
    Name = models.CharField(max_length=255)
    BookingDate = models.DateField()
    No_of_guests = models.IntegerField()

class Menu(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.IntegerField()
    Inventory = models.IntegerField()
    