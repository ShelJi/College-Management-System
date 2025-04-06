from django.urls import path
from student_dashboard.views import (DashboardView,
                                    ProfileView,
                                    AttendanceView)



app_name = 'student_dashboard'


urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('attendance/', AttendanceView.as_view(), name='attendance')
]