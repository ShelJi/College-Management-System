from django.urls import path
from exam.views import (AllExamView,
                        CreateExamView,
                        DetailExamView,
                        StudentExamView,
                        CreateResultView,
                        ExamResultView)


app_name = "exam"


urlpatterns = [
    path('', AllExamView.as_view(), name="all_exam"),
    path('new/', CreateExamView.as_view(), name="create_exam"),
    path('view/<int:pk>/', DetailExamView.as_view(), name="view_exam"),
    path('student/', StudentExamView.as_view(), name="student_exam"),
    
    path("create-result/", CreateResultView.as_view(), name="create_result"),
    path("result/<int:pk>/<int:student>/", ExamResultView.as_view(), name="exam_result"),
]
