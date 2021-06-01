from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import employee,meeting
from django import forms
from django.db.models import F
from .forms import AForm
# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created: {username}")
            employee.objects.create(name=username)
            login(request, user)
            messages.info(request, f"You are now logged in as {username}")
            print("yaaa!")
            return redirect("../upload/")
        else:    
            password1 = form.data['password1']
            password2 = form.data['password2']
            for msg in form.errors.as_data():
                if msg == 'email':
                    messages.error(request, f"Declared {email} is not valid")
                if msg == 'password2' and password1 == password2:
                    messages.error(request, f"Selected password: {password1} is not strong enough")
                elif msg == 'password2' and password1 != password2:
                    messages.error(request,
                                   f"Password: '{password1}' and Confirmation Password: '{password2}' do not match")
                else:
                    messages.error(request,
                                   f"Error")
    form = UserCreationForm
    return render(request=request,
                  template_name="employee/register.html",
                  context={"form": form})



def login_request(request):
    if request.user.is_authenticated:
        return redirect('../upload/')
    if request.method == 'GET':
        print('fneriu44')
        form = AuthenticationForm()
        return render(request, 'employee/login.html', {'form': form})
    if request.method == 'POST':
        print("egniurnbriubnrtbuirnbruibnrsbrs")
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('../upload/')
            else:
                print("Can i get a hooyaa")
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm(data=request.POST)
    return render(request,
                  "employee/login.html",
                  {"form": form})

def profile_view(request, id):
    obj = employee.objects.get(id=id)
    context = {
        "con": obj,
    }
    return render(request, "employee/profile.html", context)
def dashboard_view(request,id):
    obj = employee.objects.get(id=id)
    all_meets = obj.meetings.values()
    context={
        "con":obj,
        "all": all_meets,
    }
    return render(request,"employee/dashboard.html",context)
def schedule_view(request,id):
    obj= employee.objects.get(id=id)
    all_meets = obj.meetings.values()
    context = {
        "con": obj,
        "all": all_meets,
    }
    return render(request,"employee/schedule.html",context)