# from django import forms
# from shop.models import Order

# # class OrderForm(forms.Form): #forms.ModelForm
# #     name = forms.CharField(max_length=150)
# #     phone = forms.CharField(max_length=20)
# #     quantity = forms.IntegerField(blank = True)


# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         # fields = ['name','phone','quantity']  
#         exclude = ('created_at','updated_at','product')

from django import forms
from shop.models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone', 'quantity']  # Qo'llaniladigan maydonlar
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'}),
        }