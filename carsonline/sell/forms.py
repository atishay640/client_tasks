from django import forms
from .models import Car, PurchaseOrder

class ListCarForm(forms.ModelForm):

    class Meta: 
        model = Car 
        fields = "__all__"
        exclude = ("currency", "status")


class BuyCarForm(forms.ModelForm):

    class Meta: 
        model = PurchaseOrder 
        fields = "__all__"
        exclude = ("status", "car")