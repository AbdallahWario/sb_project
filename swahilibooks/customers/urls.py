from django.urls import path,include
from . import views

urlpatterns = [
    path('customers', views.customerList,name='customers'),
]
