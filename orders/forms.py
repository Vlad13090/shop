from django import forms


class OrderForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    number = forms.CharField()
    delivery = forms.CharField()
    address = forms.CharField(required=False)
    paid = forms.BooleanField()



