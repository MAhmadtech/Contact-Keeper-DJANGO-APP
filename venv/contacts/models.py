from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Contact(models.Model):
    contact_holder = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    contact_type = models.CharField(max_length=20)
    

    def __str__(self):
        return self.name