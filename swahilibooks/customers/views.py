from django.shortcuts import render
from .models import Customer


def customerList(request):
    all_customers = Customer.objects.all()
    context={
        'all_customers':all_customers
    }
    
    return render(request,'customers/customers.html',context)