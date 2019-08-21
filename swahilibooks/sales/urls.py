from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index, name = 'sales'),
    path('sales', views.sales,name='sales'),
    path('add_sales', views.add_sales,name='add_sales'),
    path('register', views.add_sales,name='add_sales'),
    #path('rem_sales', views.rem_sales,name='rem_sales'),
]
