from django.urls import path
from . import views

urlpatterns = [
    path('Contactinfo', views.contact, name='contact'),
]
