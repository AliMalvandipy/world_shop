from django import forms

class AddToCartProductForm(forms.Form):
    QUANTITY_cHOICES = [(i, str(i)) for i in range(1,31)] 

    quantity = forms.TypedChoiceField(choices=QUANTITY_cHOICES, coerce=int)
    
    inplace = forms.BooleanField(required=False, widget= forms.HiddenInput)