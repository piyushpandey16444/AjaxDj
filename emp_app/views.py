from django.shortcuts import render

def home(request):
    return render(request, 'emp_app/index.html')