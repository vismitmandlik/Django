from django.urls import path, include
from .views import  getFlight
urlpatterns = [
    path('',getFlight,name='getFlight')
]