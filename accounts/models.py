"""Staff and Student models for user management."""
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

from core.choices import (DISTRICT_CHOICES, 
                          STATE_CHOICES,
                          COURSE_CHOICES, 
                          SEMESTER_CHOICES)


class UserManagementModel(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    address = models.CharField(max_length=100)
    district = models.CharField(max_length=50, choices=DISTRICT_CHOICES)
    state = models.CharField(max_length=50, choices=STATE_CHOICES)
    pincode = models.CharField(max_length=6, blank=True, null=True)

    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        """Ensure username and email are always saved in lowercase."""
        if self.username:
            self.username = self.username.lower()
        if self.email:
            self.email = self.email.lower()
        super().save(*args, **kwargs)

    def __str__(self):
        # return f"{self.username} - {'Staff' if self.is_staff else 'Student'}"
        return f"{self.username}"


class StudentModel(models.Model):
    user = models.OneToOneField(UserManagementModel, on_delete=models.CASCADE, related_name="student_profile")
    rollno = models.CharField(max_length=50, unique=True, null=True, blank=True)

    academic_fee = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    exam_fee = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    hostel_fee = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    transport_fee = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    other_fee = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    balance_fee = models.IntegerField(validators=[MinValueValidator(0)], default=0)

    course = models.CharField(max_length=100, choices=COURSE_CHOICES)
    semester = models.CharField(max_length=20, choices=SEMESTER_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Joined")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Last Updated")
    
    class Meta:
        verbose_name_plural = "Students"

    def total_fee(self):
        """Calculate total fee including all components."""
        return sum(filter(None, [self.academic_fee, self.exam_fee, self.hostel_fee, self.transport_fee, self.other_fee]))
    
    def save(self, *args, **kwargs):
        last_user = StudentModel.objects.order_by('-id').first()
        last_rollno = int(last_user.rollno[3:]) if last_user and last_user.rollno else 1000 
        self.rollno = f"COL{last_rollno + 1}" 
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.course} - Semester {self.semester}"


class StaffModel(models.Model):
    user = models.OneToOneField(UserManagementModel, on_delete=models.CASCADE, related_name="staff_profile")
    rollno = models.CharField(max_length=50, unique=True, null=True, blank=True)

    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Joined")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Last Updated")
    
    class Meta:
        verbose_name_plural = "Staff"
        
    def save(self, *args, **kwargs):
        last_user = StaffModel.objects.order_by('-id').first()
        last_rollno = int(last_user.rollno[3:]) if last_user and last_user.rollno else 1000 
        self.rollno = f"STU{last_rollno + 1}" 
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.department} - {self.designation}"