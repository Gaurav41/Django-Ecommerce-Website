from django import forms
from django.core import validators


class ContactForm(forms.Form):  
    name = forms.CharField(label="First name",max_length=50,)  
    email  = forms.EmailField(label="Email", max_length = 254,validators=[validators.EmailValidator])
    message = forms.CharField(label="Message",max_length = 500)  

    #Validation #DataFlair
    # def clean_name(self):
    #     name = self.cleaned_data['name']
    #     if len(name) < 5:
    #         raise forms.ValidationError("name is too short")
    #     return name