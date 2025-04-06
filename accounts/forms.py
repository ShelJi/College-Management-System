from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import UserManagementModel


class UserManagementCreationForm(UserCreationForm):
    class Meta:
        model = UserManagementModel
        fields = ['username', 'email', 'phone', 'address', 'district', 'state', 'pincode', 'profile_pic']
