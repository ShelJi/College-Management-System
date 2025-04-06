from django.db import models
from django.contrib.auth import get_user_model
from core.choices import SEMESTER_CHOICES


User = get_user_model()


class AttendanceModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    semester = models.CharField(choices=SEMESTER_CHOICES, max_length=50)
    total_days = models.IntegerField()
    attended = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


# class 