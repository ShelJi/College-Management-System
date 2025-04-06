from django.urls import path
from .views import (
    DashboardView,
    AddStudentView,
    StudentListView,
    StudentDetailView,
    CreateAttendanceView,
    ListAttendanceView,
    
)

app_name = 'staff_dashboard'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('students/', StudentListView.as_view(), name='list_students'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='view_student'),
    path('add-student/', AddStudentView.as_view(), name='add_student'),
    path('add-attendance/<int:pk>/', CreateAttendanceView.as_view(), name='create_attendance'),
    path('list-attendance/<int:pk>/', ListAttendanceView.as_view(), name='attendance_list'),
]
