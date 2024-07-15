from django.urls import path
from .views import StudentListView
from .views import ClassPeriodListView
from .views import CourseListView

urlpatterns=[
    path("student/", StudentListView.as_view(),name='student_list_view'),
    path("classperiod/",ClassPeriodListView.as_View(),name='classperiod'),
    path("course/",Course.as_view(), name='course'),
]