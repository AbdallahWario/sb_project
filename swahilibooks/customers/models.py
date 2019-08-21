from django.db import models


class Customer(models.Model):
    customer_name = models.CharField(max_length=50)
    email_address = models.CharField(max_length=50,blank=True)
    phone_number = models.CharField(max_length=12 )
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.customer_name
  