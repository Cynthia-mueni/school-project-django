from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField(max_length=15)
    age=models.IntegerField()
    counrty=models.CharField()
    gender=models.CharField()
    bio=models.TimeField()
    date_of_birth=models.DateField()


def __str__(self):
        return f"{self.first_name} {self.last_name}"