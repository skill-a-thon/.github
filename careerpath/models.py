from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=128)
    image_link = models.CharField(max_length=512)
    description = models.CharField(max_length=1024)
    
class Mentor(models.Model):
    mentor_name = models.CharField(max_length=128)
    image_link = models.CharField(max_length=512)
    description = models.CharField(max_length=1024)

class User(AbstractUser):
    is_student = models.BooleanField(default=False)

class UserCourses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    courses = models.ManyToManyField(Course, blank=True, related_name="cart_item")

class UserMentor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    mentor = models.ManyToManyField(Mentor, blank=True, related_name="cart_item")