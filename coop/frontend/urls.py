from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ),
    # here is where we should have the login page, cart, cycle, add product, etc
]
