from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    person={
        'name':'Amal Dev',
        'age':20,
        'place':'pgdi'
    }
    return render(request,'index.html',person)


def service(request):
    numbers=[1,2,3,4,5,6,7,8,9]
    context = {
        "numbers":numbers
    }
    return render(request,'service.html',context)

def contact(request):
     return render(request,'contact.html')