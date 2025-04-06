from django import forms
from student_dashboard.models import AttendanceModel

class AttendanceForm(forms.ModelForm):
    """Form for marking student attendance based on pk."""

    class Meta:
        model = AttendanceModel
        fields = ['semester', 'total_days', 'attended']