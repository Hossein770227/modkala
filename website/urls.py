from django.urls import path

from . import views

app_name ='website'

urlpatterns = [
    path('welcome/', views.welcome_to_website, name='welcome'),
]
