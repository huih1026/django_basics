# forms.ModelForm
# forms.Form
from django import forms
from .models import Participant


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['firstname', 'lastname', 'email']


# class RegisterAnotherForm(forms.Form):
#     first_name = forms.CharField(max_length=50)
#     last_name = forms.CharField(max_length=50)
#     email = forms.EmailField(unique=True)
