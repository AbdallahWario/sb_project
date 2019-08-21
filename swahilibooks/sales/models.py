from django.db import models
from datetime import datetime



class Sales(models.Model):
    PRODUCT = models.CharField(max_length=50)
    DESCRIPTION = models.CharField(max_length=50)
    QUANTITY = models.IntegerField()
    RATE = models.DecimalField(max_digits=7,decimal_places=2)
    AMOUNT = models.DecimalField(max_digits=7,decimal_places=2)
    # subtotal = models.DecimalField(max_digits=7,decimal_places=2)
    # shipping = models.DecimalField(max_digits=7,decimal_places=2)
   # total = models.DecimalField(max_digits=7,decimal_places=2)

    
    #address = models.CharField(max_length=200)
    #date = models.DateTimeField(default=datetime.now,blank=True)
    #description = models.TextField(blank=True)
    
    #phone_number = models.CharField(max_length=12 )

    def __str__(self):
        return self.PRODUCT


