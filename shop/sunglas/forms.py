from django import forms
from .models import shoping, product, Contacts

# forms using required field and validation forms.
# Registration form validations.

class market(forms.ModelForm):
    class Meta:
        model = shoping
        fields = ['name', 'email', 'address', 'phone', 'password', 'gender']
        labels = {'name': 'Enter Your Name', 'password': 'Enter Your Password',
                  'email': 'Enter your Email', 'address': 'Enter Your Address'}
        help_text = {'name': 'Enter Your Full Name'}
        error_messages = {'name':  {'required': 'Please enter your name'},
                          'email': {'required': 'Please enter your email'}}
        widgets = {'password': forms.PasswordInput, 'name': forms.TextInput(attrs={'class': 'myclass', 'placeholder': 'Enter your name'}),}

class products(forms.ModelForm):
    class Meta:
        model = product
        fields = ['name', 'price', 'categary', 'images']

class conts(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['name', 'phone', 'email', 'messages']
        labels = {'name': 'Enter Your Name', 'email': 'Enter your Email', 'messages': 'Enter Your messages'}