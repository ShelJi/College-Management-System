from django import forms
from review.models import (ReviewModel,
                           SurveyResponse)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewModel
        fields = ["review"]
        widgets = {
            "review": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }


class SurveyForm(forms.ModelForm):
    class Meta:
        model = SurveyResponse
        fields = '__all__'
        exclude = ['user', 'submitted_at']
