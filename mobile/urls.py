from django.urls import path

from . import views

app_name = 'mobile'

urlpatterns = [
    path('', views.mobile_list, name='mobile_list'),
]
