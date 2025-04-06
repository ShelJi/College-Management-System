import random
from datetime import date
from django.db import models
from core.choices import (SEMESTER_CHOICES,
                          COURSE_CHOICES)
from django.contrib.auth import get_user_model


User = get_user_model()


def generate_unique_exam_id():
    while True:
        exam_id = f"NI-{random.randint(1000, 9999)}"
        if not ExamModel.objects.filter(exam_id=exam_id).exists():
            return exam_id
        
def choices_generator():
    return [(e.id, str(e)) for e in ExamModel.objects.all()]


class ExamManager(models.Manager):
    def get_queryset(self):
        queryset = super().get_queryset()
        for exam in queryset.filter(status=True, date__lt=date.today()):
            exam.status_activity()
            exam.save()
        return queryset


class ExamModel(models.Model):
    exam_id = models.CharField(max_length=10, unique=True, default=generate_unique_exam_id, editable=False)
    semester = models.CharField(max_length=50, choices=SEMESTER_CHOICES)
    
    department = models.CharField(choices = COURSE_CHOICES, max_length=50)

    subject1 = models.CharField(max_length=50)
    subject2 = models.CharField(max_length=50, null=True, blank=True)
    subject3 = models.CharField(max_length=50, null=True, blank=True)
    subject4 = models.CharField(max_length=50, null=True, blank=True)
    subject5 = models.CharField(max_length=50, null=True, blank=True)
    subject6 = models.CharField(max_length=50, null=True, blank=True)
    subject7 = models.CharField(max_length=50, null=True, blank=True)
    subject8 = models.CharField(max_length=50, null=True, blank=True)
    subject9 = models.CharField(max_length=50, null=True, blank=True)
    total_marks = models.CharField(max_length=50)
    
    date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    start_time = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    end_time = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    status = models.BooleanField(default=True)
    
    objects = ExamManager() 
    
    
    def status_activity(self):
        """If exam is active check for the dates and deactivate if date passed automatically."""

        if self.status and self.date < date.today():
            self.status = False
            self.save()
        
    def __str__(self):
        return f"{self.semester} - {self.exam_id}"
    

class ExamResultModel(models.Model):
    # exam_id = models.CharField(max_length=50, choices= choices_generator)
    exam = models.ForeignKey(ExamModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mark_subject1 = models.CharField(max_length=50, null=True, blank=True)
    mark_subject2 = models.CharField(max_length=50, null=True, blank=True)
    mark_subject3 = models.CharField(max_length=50, null=True, blank=True)
    mark_subject4 = models.CharField(max_length=50, null=True, blank=True)
    mark_subject5 = models.CharField(max_length=50, null=True, blank=True)
    mark_subject6 = models.CharField(max_length=50, null=True, blank=True)
    mark_subject7 = models.CharField(max_length=50, null=True, blank=True)
    mark_subject8 = models.CharField(max_length=50, null=True, blank=True)
    mark_subject9 = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.exam_id}"
    

