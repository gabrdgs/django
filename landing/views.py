from django.shortcuts import render

# Create your views here.

def mostrar_index(request):
    return render(request,'index.html')

def mostrar_about(request):
    return render(request,'about.html')