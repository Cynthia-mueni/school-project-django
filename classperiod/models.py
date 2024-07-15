from django.db import models



class ClassPeriod(models.Model):
    start_time = models.DateTimeRangeFieldField()
    end_time = models.TimeField()
    courseroom=models.CharField(max_length=20)
    course=models.CharField(max_length=20)
    day_of_week = models.CharField(max_leghth=10)
    
    def __str__(self):
        return f"{self.start_time} {self.day_of_week}"

# Create your models here.
