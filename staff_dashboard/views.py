from django.urls import reverse_lazy
from django.views.generic import (TemplateView,
                                  CreateView,)

from accounts.models import (UserManagementModel,
                             StudentModel)
from accounts.forms import UserManagementCreationForm

from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from accounts.models import StudentModel
from student_dashboard.models import (AttendanceModel)
from staff_dashboard.forms import (AttendanceForm)
from staff_dashboard.mixins import StaffRequiredMixin


class DashboardView(StaffRequiredMixin, TemplateView):
    template_name = 'staff_dashboard/dashboard.html'
    
    
class AddStudentView(StaffRequiredMixin, CreateView):
    template_name = 'staff_dashboard/add_student.html'
    model = UserManagementModel
    form_class = UserManagementCreationForm
    success_url = reverse_lazy('staff_dashboard:dashboard')

    def form_valid(self, form):
        response = super().form_valid(form)

        course = self.request.POST.get("course")
        semester = self.request.POST.get("semester")
        academic_fee = self.request.POST.get("academic_fee", 0)
        exam_fee = self.request.POST.get("exam_fee", 0)
        hostel_fee = self.request.POST.get("hostel_fee", 0)
        transport_fee = self.request.POST.get("transport_fee", 0)
        other_fee = self.request.POST.get("other_fee", 0)
        balance_fee = self.request.POST.get("balance_fee", 0)

        StudentModel.objects.create(
            user=self.object, 
            course=course, 
            semester=semester,
            academic_fee=academic_fee, 
            exam_fee=exam_fee, 
            hostel_fee=hostel_fee, 
            transport_fee=transport_fee, 
            other_fee=other_fee, 
            balance_fee=balance_fee
        )

        return response
    

class StudentListView(StaffRequiredMixin, ListView):
    model = StudentModel
    template_name = 'staff_dashboard/student_list.html'
    context_object_name = 'students'
    ordering = ['rollno'] 
    

class StudentDetailView(StaffRequiredMixin, DetailView):
    model = StudentModel
    template_name = 'staff_dashboard/view_student.html'
    context_object_name = 'student'

    def get_object(self):
        return get_object_or_404(StudentModel, id=self.kwargs['pk'])
    
    
class CreateAttendanceView(StaffRequiredMixin, CreateView):
    """View for staff to create attendance records for a specific student."""
    
    model = AttendanceModel
    form_class = AttendanceForm
    template_name = "staff_dashboard/create_attendance.html"
    success_url = reverse_lazy("staff_dashboard:list_students")  

    def form_valid(self, form):
        """Ensure the attendance record is linked to the correct student."""
        student = get_object_or_404(StudentModel, pk=self.kwargs["pk"])
        form.instance.user = student.user
        return super().form_valid(form)
    
    
class ListAttendanceView(StaffRequiredMixin, ListView):
    model = AttendanceModel
    template_name = 'staff_dashboard/attendance_list.html'
    context_object_name = 'attendances'

    def get_queryset(self):
        student = get_object_or_404(StudentModel, id=self.kwargs['pk'])
        qs = AttendanceModel.objects.filter(user=student.user)
        return qs if qs.exists() else None
