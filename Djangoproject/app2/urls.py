from django.urls import path,include
from . import views
urlpatterns = [
    path("vismit/",views.vismit,name="vismit"),
    # path("newpage/",views.newpage,name="newpage")
]