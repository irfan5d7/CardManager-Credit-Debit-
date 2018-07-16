from django import forms
from django.forms import DateInput

from CardsWallet.models import Cards


class AddCard(forms.ModelForms):
    class Meta:
        model = Cards
        exclude = ['user','id']
        widgets ={
            'name_on_the_card': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name on the card'}),
            'card_number' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Card Number'}),
            'cvv' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'cvv'}),
            'expiry_date' :  DateInput(attrs={'type': 'date'}),
            'type' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type'}),
        }