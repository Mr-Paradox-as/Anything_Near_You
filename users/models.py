from django.db import models

# Create your models here.

class Profile(models.Model):
    first_name= models.CharField(max_length=100)
    last_name = models.CharField(max_length=50,blank=True)
    username = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    bio = models.CharField(max_length=500, blank=True)
    linkedin = models.URLField(blank=True)
    instagram = models.URLField(blank=True)

    def __str__(self):
        return str(self.first_name)
    

# class Resource(models.Model):
#     owner = models.OneToOneField(Profile, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     description = models.CharField(max_length=500)
