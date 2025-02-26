from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Meep, Profile


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class ProfileEditForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfilePicForm(forms.ModelForm):
    profile_image = forms.ImageField(
        label='',
        widget=forms.widgets.FileInput()
    )
    
    class Meta:
        model = Profile
        fields = ['profile_image']


class MeepForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        label="",
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Type your meep here!",
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = Meep
        exclude = ['user', 'likes']
