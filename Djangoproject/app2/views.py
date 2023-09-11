from django.shortcuts import render
from django.http import HttpResponse
# from django.shortcuts import render
# Create your views here.
# def vismit(request):
#     return HttpResponse('<h1>Hello:</h1>')

def vismit(request):
    content=[
        {"id":"21ce068","name":"Vismit","Branch":"CE"},
        {"id":"21ce061","name":"Dhruvi","Branch":"CE"}
    ]
    return render(request,"page.html",{"context":content})