from django.urls import path
from accounts.views import (CustomLoginView)
from django.contrib.auth.views import LogoutView


app_name = 'accounts'


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page="landing_page:index"), name='logout'),
]