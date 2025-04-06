from django.views.generic import (TemplateView,
                                  DetailView,
                                  ListView)
from accounts.models import StudentModel
from student_dashboard.models import AttendanceModel
from django.shortcuts import get_object_or_404
from student_dashboard.mixins import StudentRequiredMixin


class DashboardView(StudentRequiredMixin, TemplateView):
    template_name = 'student_dashboard/dashboard.html'
    

class ProfileView(StudentRequiredMixin, DetailView):
    model = StudentModel
    template_name = 'student_dashboard/profile.html'
    context_object_name = 'student'

    def get_object(self):
        """Ensure students can only view their own profile."""
        return get_object_or_404(StudentModel, user=self.request.user)


class AttendanceView(StudentRequiredMixin, ListView):
    """View to display attendance records for students."""

    model = AttendanceModel
    template_name = "student_dashboard/attendance.html"
    context_object_name = "attendance_records"

    def get_queryset(self):
        """Return attendance records for the logged-in student only."""
        user = self.request.user
        if AttendanceModel.objects.filter(user=user).exists():
            print(AttendanceModel.objects.filter(user=user))
            return AttendanceModel.objects.filter(user=user)
        return AttendanceModel.objects.none()