from django import forms
from registration.models import UserInformation

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInformation
        fields = "__all__"

class SignInForm(forms.ModelForm):
    class Meta:
        model = UserInformation
        exclude = ["firstname", "lastname"]