from django.urls import path
from review.views import (AllReview,
                          NewReview,
                          SurveyCreateView,
                          SurveyListView,
                          SurveyDetailView)
from django.views.generic import TemplateView


app_name = "review"


urlpatterns = [
    path('', AllReview.as_view(), name="all_reviews"),
    path('new/', NewReview.as_view(), name="new_review"),
    path("survey/", SurveyCreateView.as_view(), name="survey_create"),
    path("survey/list/", SurveyListView.as_view(), name="survey_list"),
    path("survey/detail/<int:pk>/", SurveyDetailView.as_view(), name="survey_detail"),
    path("survey/thank-you/", TemplateView.as_view(template_name="review/survey_thank_you.html"), name="survey_thank_you"),
]

