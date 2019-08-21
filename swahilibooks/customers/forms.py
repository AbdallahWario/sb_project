from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    
    class Meta:
        model = customer

        fields = [ " customer_name","email_address ", "phone_number ", "address"]
