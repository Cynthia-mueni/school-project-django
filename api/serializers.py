from rest_framework import serializers
from student.models import Student
from teacher.models import Teacher
from course.models import Course
from classperiod.models import ClassPeriod


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Student
        fields="__all__"
        
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Teacher
        fields="__all__"
        
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        Model= Course
        fields="__all__"
        
class ClassPeriod(serializers.ModelSerializer):
    class Meta:
        Module=ClassPeriod
        fields="__all__"
    


        