from django.shortcuts import render, redirect
from .models import Sales
from .forms import SalesForm
from .forms import SalesForm 
from django.http import HttpResponse
from django.forms import ModelForm

def sales(request):
     all_sales = Sales.objects.all()

     context = {
        'all_sales':all_sales
     }
     return render(request,'sales/sales.html',context)

def add_sales(request):
    pass

# def add_sales(request):
#     if request.method == "POST":
#         item = request.POST['item']
#         unit_price = int(request.POST['unit_price'])
#         quantity = request.POST['quantity']
#         totals = request.POST['totals']

#         sales = Sales(Item=item,unit_price=unit_price, quantity=quantity, totals=totals)
#         sales.save()

#         return redirect('register')

    # if request.method == 'POST':
    #     form = SalesForm(request.POST or None)

    #     if form.is_valid():
    #         form.save()
            
    #         all_sales = Sales.objects.all()

    #         context = {
    #         'all_sales':all_sales
    #         }
   
    #         # return render(request,'sales/sales.html',context)
    #         return HttpResponse('hello world')
    # else:
    #     return HttpResponse('hello world')
"""

    Item = request.POST['Item']
    unit_price = request.POST['unit_price']
    totals = request.POST['totals']
    subtotal = request.POST['subtotal']
    shipping = request.POST['shipping']
    total = request.POST['total']

    sales = (Item=Item,unit_price=unit_price , totals = totals , subtotal = subtotal ,shipping = shipping , total = total)
    sales.save()

   return render(request,'sales/sales.html',context)
"""



"""

def sales(request):
    all_sales = Sales.objects.all()

    context = {
        'all_sales':all_sales
    }

    return render(request,'sales/sales.html',context)
"""

def index(request):
    return render(request,'index/index.html')

def  total(request):
    if request.method == 'POST':
        form = SalesForm

        if form.is_valid():
            form.save()
            all_sales = Sales.objects.all()
            messages.success(request,('one item has been added to sales!'))
            return render(request,'sales/sales.html,context')
        else:
            all_sales = Sales.objects.all()
            return render(request,'sales/sales.html,context')

            
def totals_data(self):
        return self.aggregate(Sum("total"), Avg("total"))