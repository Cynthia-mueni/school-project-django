from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import Student
from course.models import Course
from teacher.models import Teacher
from classperiod.models import ClassPeriod
from .serializers import StudentSerializer
from .serializers import TeacherSerializer
from .serializers import ClassPeriodSerializer


class StudentListView (APIView):
    def get(self,request):
        students=Student.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data)


class TeacherListView (APIView):
    def get (self,request):
        teachers=Teacher.objects.all()
        serializer=TeacherSerializer (teachers,many=True)
        return Response(serializer.data)
    
class CourseListView (APIView):
    def get (self,request):
        courses=Course.objects.all()
        serializer=CourseSerializer (courses,many=True)
        return Response(serializer.data)

class ClassPeriod(APIView):
    def get (self,request):
        classperiod=classperiod.object.all()
        serializer=ClassPeriod(classperiod,many=True)
        return Response(serializer.data)
    
# class Class(APIView):
#     def get (self,request):
#         classes=Class.object.all()
#         serializer=Class (classes,man=True)
#         return Response(serializer.data)
    

# Create your views here.
