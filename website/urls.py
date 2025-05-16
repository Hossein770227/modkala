from django.urls import path

from . import views

app_name ='website'

urlpatterns = [
    path('welcome/', views.WelcomeToWebsite.as_view(), name='welcome'),
]
