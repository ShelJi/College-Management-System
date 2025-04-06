from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin)
from django.shortcuts import redirect
from django.urls import reverse


class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """Mixin to restrict access to staff users only."""
    
    def test_func(self):
        return self.request.user.is_staff 
    
    def handle_no_permission(self):
        return redirect(reverse("core:invalid_access"))
    