from django.urls import path
from django.urls import include
from . import views

app_name = "TasksApp"


urlpatterns = [
    path("", views.index, name = "index" ),
    path("add", views.add, name = "add"),
    

]