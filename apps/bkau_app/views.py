from django.shortcuts import render, redirect

def index(request):
    return render(request, 'bkau_app/index.html')
