from django.db import models

# Create your models here.
class login_tb(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    utype=models.CharField(max_length=30)

class volunteer_tb(models.Model):
    name=models.CharField(max_length=30)  
    age=models.CharField(max_length=30)
    Phone=models.BigIntegerField()   
    State=models.CharField(max_length=30)
    District=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    date=models.DateTimeField(auto_now_add=True)  

class police_tb(models.Model):
    name=models.CharField(max_length=30)  
    age=models.CharField(max_length=30)
    Phone=models.BigIntegerField()   
    State=models.CharField(max_length=30)
    District=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    date=models.DateTimeField(auto_now_add=True) 

class member_tb(models.Model):
    name=models.CharField(max_length=30)  
    Phone=models.BigIntegerField() 
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)  
    address=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    State=models.CharField(max_length=30)
    District=models.CharField(max_length=30)
    date=models.DateTimeField(auto_now_add=True)      

class message_tb(models.Model):
    location=models.CharField(max_length=30) 
    police=models.CharField(max_length=30)
    image=models.ImageField() 
    date=models.DateTimeField(auto_now_add=True)    

class penalty_tb(models.Model):
    name=models.CharField(max_length=30)  
    address=models.CharField(max_length=30)
    District=models.CharField(max_length=30)
    State=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    image=models.ImageField() 
    penalty=models.CharField(max_length=30,)
    date=models.DateTimeField(auto_now_add=True) 

class campaign_tb(models.Model):
    location=models.CharField(max_length=30) 
    chief_guest=models.CharField(max_length=30)
    Description=models.CharField(max_length=30)
    image=models.ImageField() 
    date=models.DateTimeField(auto_now_add=True)  

class rehab_tb(models.Model):
    member_username=models.CharField(max_length=30) 
    rehab_location=models.CharField(max_length=30)
    start_date=models.DateField(max_length=30)
    end_date=models.DateField() 
    police=models.CharField(max_length=30)
    address=models.CharField(max_length=30)

class form(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)    

