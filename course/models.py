from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=10, unique=True)
    description = models.TextField()
    scores = models.PositiveIntegerField()
    department = models.CharField(max_length=50)
    trainer = models.CharField(max_length=20)
    is_elective = models.BooleanField(default=False)
    prerequisites = models.TextField()
    
    
def __str__(self):
        return f"{self.course_name} {self.course_code}"