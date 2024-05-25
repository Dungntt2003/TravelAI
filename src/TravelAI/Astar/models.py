from django.db import models
# from django.contrib.auth.models import AbstractUser, BaseUserManager


# # Create your models here.

# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     des = models.TextField()
#     def __str__(self):
#         return self.name
    
class Astar_user(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    def __str__(self):
        return self.email
