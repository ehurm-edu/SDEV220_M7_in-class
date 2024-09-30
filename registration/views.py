from django.shortcuts import render
from registration import forms, models

# Create your views here.
def index(request):
    return render(request, "index.html")

def regview(request):
    registration_form = forms.UserInfoForm()
    if request.method == "POST":
        registration_form = forms.UserInfoForm(data=request.POST)
        if registration_form.is_valid():
            registration_form.save(commit=True)
        else:
            print("Something is wrong")

    reg_dictionary = {"register": registration_form}
    return render(request, "registration.html", context=reg_dictionary)
    
def loginview(request):
    login_form = forms.SignInForm()
    if request.method == "POST":
        login_form = forms.SignInForm(data=request.POST)
        if login_form.is_valid():
            login_form.save(commit=True)
        else:
            print("Something is wrong")

    login_dictionary = {"login": login_form}
    return render(request, "login.html", context=login_dictionary)