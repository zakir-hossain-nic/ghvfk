from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse('This is About page')

def contact(request):
    return HttpResponse('This is Contact page')
