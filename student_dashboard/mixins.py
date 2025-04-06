from django.urls import reverse
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin)
from django.shortcuts import redirect


class StudentRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """Mixin to restrict access to student users only."""
    
    def test_func(self):
        return not self.request.user.is_staff 

    def handle_no_permission(self):
        return redirect(reverse("core:invalid_access"))