from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from zeal.models import Record


class Signup_user_form(UserCreationForm):

    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    username = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'username'}), help_text='<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>')
    password1 = forms.CharField(label="", max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'password'}), help_text='<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>')
    password2 = forms.CharField(label="", max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'confirm password'}), help_text='<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>')

    class Meta:

        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")


class AddRecordForm(forms.ModelForm):

    first_name = forms.CharField(required=True, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(required=True, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    email = forms.EmailField(required=True, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    phone_number = forms.CharField(required=True, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone number'}))
    address = forms.CharField(required=True, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}))
    city = forms.CharField(required=True, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}))
    state = forms.CharField(required=True, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'State'}))
    zipcode = forms.CharField(required=True, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'zipcode'}))

    class Meta:

        model = Record
        #fields= ("first_name", "last_name", "email", "phone", "address", "city", "state", "zipcode")
        exclude = ("user",)