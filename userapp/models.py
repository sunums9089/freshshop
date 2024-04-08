from django.db import models
from adminapp.models import *

# Create your models here.
class Info(models.Model):
    your_name=models.CharField(max_length=50)
    your_email=models.EmailField()
    subject=models.CharField(max_length=50)
    your_message=models.CharField(max_length=180)


class Registeration(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    contact=models.IntegerField(default=0)


class Mycart(models.Model):
    userid=models.ForeignKey(Registeration,on_delete=models.CASCADE)
    productid=models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    total=models.IntegerField()
    status=models.IntegerField(default=0)

class Checkout(models.Model):
    userid=models.ForeignKey(Registeration,on_delete=models.CASCADE)
    cartid=models.ForeignKey(Mycart,on_delete=models.CASCADE)
    address=models.CharField(max_length=200)
    country=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip1=models.IntegerField(default=0)