from django.urls import path
from core.views import InvalidAccess


app_name = 'core'


urlpatterns = [
    path('not-found/', InvalidAccess.as_view(), name="invalid_access"),
]
