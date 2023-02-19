from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    isStudent = models.BooleanField(default=False)
    isTeacher = models.BooleanField(default=False)

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        # return self.user.first_name + " " + self.user.last_name
        return self.user.username
class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    def __str__(self):
        # return self.user.first_name + " " + self.user.last_name
        return self.user.username