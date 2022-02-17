from django.shortcuts import render,redirect
from .models import *
from .forms import UserRegistrationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib import auth

# Create your views here.

def demo(request):
    # data = Homework.objects.filter(subject = 'Science')
    # data = Homework.objects.values('description')
    # data = Homework.objects.get(pk=2)
    data1 = Todo.objects.filter(title__startswith = 'wake')
    data2 = Todo.objects.filter(title__endswith = 'pm.')
    # print(data1) # debug
    # print(data2) # debug 
    
    data1_list = []
    for data in data1:
        data1_list.append(data)
    # print(l1)

    data2_list = []
    for data in data2:
        data2_list.append(data)
    # print(l2)

    dict = {
        'data1_list':data1_list,
        'data2_list':data2_list
    }

    return render(request,'dashboard/demo.html',dict)

def home(request):
    return render(request,'dashboard/home.html')

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data.get('username')
            messages.success(request,f"Acccount Created for {username}!!")
            # redirect('login')
    else:
        user_form = UserRegistrationForm() 
    context = {
        'user_form':user_form
    }
    return render(request,"dashboard/register.html",context)

