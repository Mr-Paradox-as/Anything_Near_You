from django.db import models
from users.models import Profile

# Create your models here.
class Resources(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='resources')
    title = models.CharField(max_length=200)
    discription = models.CharField(max_length=500,blank= True)

    def __str__(self):
        return self.title