from django.db import models

# Create your models here

class Signup(models.Model):
    name = models.CharField(max_length= 50)
    email = models.EmailField()
    password = models.IntegerField()
    confirmpassword = models.IntegerField()

    def __str__(self):
        return self.name
    
class PlaceOrder(models.Model):

    productname = models.CharField(max_length=120)
    quantity = models.IntegerField()
    name = models.CharField(max_length=120)
    adress = models.CharField(max_length=120)

    def __str__(self):
        return self.productname
    