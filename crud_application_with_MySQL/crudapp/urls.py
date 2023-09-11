from django.urls import path
from crudapp import views

urlpatterns = [
    path("", include('crud_')),
    
]
