from django.db import models
from datetime import datetime

# change datefield model.

class Quotations(models.Model):
    product_name = models.CharField(max_length=50)
    #customer_name = models.ForeignKey(Customer, on_delete = models.Do_NOTHING)
    address = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now,blank=True)
    quantity = models.IntegerField()
    unit_price = models.IntegerField()
    # unit_price = models.DecimalField(max_digits=7,decimal_places=2)
    # amount = models.DecimalField(max_digits=7,decimal_places=2)
    # subtotal = models.DecimalField(max_digits=7,decimal_places=2)
    # valid_until = models.DateTimeField(default=datetime.now,blank=True)
    # phone_number = models.CharField(max_length=12 )

    def __str__(self):
        return self.date
  