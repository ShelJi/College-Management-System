"""Views for the accounts app."""
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import redirect


User = get_user_model()


class CustomLoginView(LoginView):
    """Custom login view."""
    template_name = 'accounts/login.html'
    
    def dispatch(self, request, *args, **kwargs):
        """Redirect logged-in users to their respective dashboards."""
        if request.user.is_authenticated:
            return redirect(self.get_success_url())
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        """Redirect users based on their role."""
        if self.request.user.is_staff:
            return reverse_lazy('staff_dashboard:dashboard')
        return reverse_lazy('student_dashboard:dashboard')
