from django.shortcuts import render
from django.views.generic import TemplateView


class InvalidAccess(TemplateView):
    template_name = "error/invalid_access.html"

