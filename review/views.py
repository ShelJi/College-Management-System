from staff_dashboard.mixins import StaffRequiredMixin
from student_dashboard.mixins import StudentRequiredMixin
from django.views.generic import (ListView,
                                  CreateView,
                                  DetailView)
from review.models import (ReviewModel,
                           SurveyResponse)
from review.forms import (ReviewForm,
                          SurveyForm)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class AllReview(StaffRequiredMixin, ListView):
    model = ReviewModel
    template_name = "review/all_reviews.html"
    context_object_name = "reviews"
    ordering = ["-created_at"]
   
   
class NewReview(StudentRequiredMixin, CreateView):
    model = ReviewModel
    form_class = ReviewForm
    template_name = "review/new_review.html"
    success_url = reverse_lazy("student_dashboard:dashboard")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class SurveyCreateView(LoginRequiredMixin, CreateView):
    model = SurveyResponse
    form_class = SurveyForm
    template_name = "review/survey_form.html"
    success_url = reverse_lazy("survey_thank_you")

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)


class SurveyListView(StaffRequiredMixin, ListView):
    model = SurveyResponse
    template_name = "review/survey_list.html"
    context_object_name = "surveys"
    ordering = ["-submitted_at"]


class SurveyDetailView(LoginRequiredMixin, DetailView):
    model = SurveyResponse
    template_name = "review/survey_detail.html"
    context_object_name = "surveys"