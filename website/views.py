from django.shortcuts import render
from django.views.generic import TemplateView

class WelcomeToWebsite(TemplateView):
    template_name = 'website/welcome.html'
