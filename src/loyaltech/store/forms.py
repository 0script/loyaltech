from django import forms

class OrderForm(forms.Form):
    customer_name=forms.CharField(
        max_length=50,
        required=True,
        label='Name',
        
        widget=forms.TextInput(
            attrs={
                'placeholder':'Enter Your Name',
                'class':'input-name',
                }
            )
    )

    customer_phone=forms.CharField(
        max_length=15,
        required=True,
        label='Phone',
        
        widget=forms.TextInput(
            attrs={
                'placeholder':'Enter Your Phone Number',
                'class':'Phone Number',
                }
            )
    )

    customer_addr=forms.CharField(
        max_length=30,
        required=True,
        label='Address',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Enter Your Location',
                'class':'Addresse',
                }
            )
    )