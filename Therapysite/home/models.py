from django.db import models
from datetime import datetime

# Create your models here.
class Plans(models.Model):
    title = models.CharField(max_length=25)
    sessions = models.CharField(max_length=100)
    descri = models.CharField(max_length=100)
    price = models.IntegerField()
    sessionprice = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title

class Counselors(models.Model):
    name = models.CharField(max_length=25)
    degree = models.CharField(max_length=100)
    special = models.CharField(max_length=100)
    expertise = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.name

class Booking(models.Model):
    name = models.CharField(max_length=25)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    counselor_name = models.ForeignKey(Counselors,on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)

class Client(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=15)
    phno=models.CharField(max_length=10)

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    phno=models.CharField(max_length=10) 

class Room(models.Model):
    name = models.CharField(max_length=1000)
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
    
