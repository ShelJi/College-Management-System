from django import forms
from exam.models import (ExamModel,
                         ExamResultModel)
from django.contrib.auth import get_user_model


User = get_user_model()


class ExamForm(forms.ModelForm):
    class Meta:
        model = ExamModel
        fields = [
            "department",
            "semester",
            "date",
            "start_time",
            "end_time",
            "subject1",
            "subject2",
            "subject3",
            "subject4",
            "subject5",
            "subject6",
            "subject7",
            "subject8",
            "subject9",
            "total_marks",
        ]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "start_time": forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
            "end_time": forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
            "status": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

class ExamResultForm(forms.ModelForm):
    class Meta:
        model = ExamResultModel
        fields = "__all__" 
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(is_staff=False) 
        