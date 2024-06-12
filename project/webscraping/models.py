from django.contrib.auth.models import AbstractUser, Group, Permission,User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_searched_location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username
    

from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django import forms
from datetime import datetime



class Weather(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    Weather_search_id = models.IntegerField(null=True)
    location = models.CharField(max_length=100)
    date1 = models.DateField(null=True)
    temp1 = models.FloatField(null=True)
    date2 = models.DateField(null=True)
    hightemp2 = models.FloatField(null=True) 
    lowtemp2 = models.FloatField(null=True)
    date3 = models.DateField(null=True)
    hightemp3 = models.FloatField(null=True) 
    lowtemp3 = models.FloatField(null=True)
    date4 = models.DateField(null=True)
    hightemp4 = models.FloatField(null=True) 
    lowtemp4 = models.FloatField(null=True)
    date5 = models.DateField(null=True)
    hightemp5 = models.FloatField(null=True) 
    lowtemp5 = models.FloatField(null=True)
    date6 = models.DateField(null=True)
    hightemp6 = models.FloatField(null=True) 
    lowtemp6 = models.FloatField(null=True)
    date7 = models.DateField(null=True)
    hightemp7 = models.FloatField(null=True) 
    lowtemp7 = models.FloatField(null=True)
    date8 = models.DateField(null=True)
    hightemp8 = models.FloatField(null=True) 
    lowtemp8 = models.FloatField(null=True)
    date9 = models.DateField(null=True)
    hightemp9 = models.FloatField(null=True) 
    lowtemp9 = models.FloatField(null=True)
    date10 = models.DateField(null=True)
    hightemp10 = models.FloatField(null=True) 
    lowtemp10 = models.FloatField(null=True)

    def __str__(self):
        return f"{self.location} - Weather Search ID: {self.Weather_search_id}"



class pricecomparator(models.Model):
    productname =models.CharField(max_length=100,null=True)
    productlink = models.URLField(null=True)
    price = models.FloatField(null=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.productname}-{self.price}-{self.productlink}"
    
class movie(models.Model):
    title = models.CharField(max_length=100,null=True)
    rating =  models.FloatField(null=True)
    summary = models.TextField(null=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return  self.title + " Rating:"+ str(self.rating)+ "/10"  
    
    
class doubtResolve(models.Model):
    doubt = models.CharField(max_length=100, null=False)
    url1 = models.URLField(null=True)
    answer1  = models.TextField(null=True)
    url2 = models.URLField(null=True)
    answer2 = models.TextField(null=True)
    url3 =  models.URLField(null=True)
    answer3 = models.TextField(null=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
