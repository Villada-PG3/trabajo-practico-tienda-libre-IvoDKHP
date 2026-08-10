from django.shortcuts import render

def home(request):
    return render(request, 'tiendalibre/home.html')

def about_me(request):
    return render(request, 'tiendalibre/about_me.html')
