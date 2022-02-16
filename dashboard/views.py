from optparse import Values
from django.shortcuts import render
from .models import *

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