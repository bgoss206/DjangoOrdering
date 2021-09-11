from django.urls import path 
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("orders/", views.orders, name="orders"),
    path("activejobs/", views.jobs, name="jobs"),
    path("orders/thanks/", views.orderThanks, name="Thanks")
]