from staff_dashboard.mixins import StaffRequiredMixin
from student_dashboard.mixins import StudentRequiredMixin
from accounts.models import StudentModel
from django.views.generic import (ListView,
                                  CreateView,
                                  DetailView)
from django.urls import reverse_lazy
from exam.models import (ExamModel,
                         ExamResultModel)
from exam.forms import (ExamForm,
                        ExamResultForm)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model


User = get_user_model()


class AllExamView(StaffRequiredMixin, ListView):
    model = ExamModel
    template_name = "exam/all_exam.html"
    context_object_name = "exams"
    
    def get_queryset(self, *args, **kwargs):
        if self.request.GET.get("status") == "1":
            return ExamModel.objects.all()
        return ExamModel.objects.filter(status=True)


class CreateExamView(StaffRequiredMixin, CreateView):
    model = ExamModel
    form_class = ExamForm
    template_name = "exam/create_exam.html"
    success_url = reverse_lazy("exam:all_exam")
    
    
class DetailExamView(DetailView):
    model = ExamModel
    template_name = "exam/detail_exam.html"
    context_object_name = "exam"
    
    
class StudentExamView(StudentRequiredMixin, ListView):
    model = ExamModel
    template_name = "exam/student_exam_list.html"
    context_object_name = "exams"
    
    
    def get_queryset(self, **kwargs):
        user = self.request.user
        student = StudentModel.objects.get(user=user)
        return ExamModel.objects.filter(department=student.course, status=True)
    
    
class CreateResultView(StaffRequiredMixin, CreateView):
    model = ExamResultModel
    form_class = ExamResultForm
    template_name = "exam/create_result.html"
    success_url = reverse_lazy("staff_dashboard:dashboard")
    

class ExamResultView(LoginRequiredMixin, ListView):
    model = ExamResultModel
    template_name = "exam/exam_result.html"
    context_object_name = "results"
    
    def get_queryset(self):
        print(self.kwargs["student"], self.kwargs["pk"])
        if self.kwargs["student"] == 1:
            student = StudentModel.objects.get(id=self.kwargs["pk"])
            user = student.user
            print(user)

        elif self.kwargs["student"] == 0:
            user = User.objects.get(id=self.kwargs["pk"])
            print(user)
            
        resultq = ExamResultModel.objects.filter(user=user)
        print("Result: ", resultq)
        return resultq
    