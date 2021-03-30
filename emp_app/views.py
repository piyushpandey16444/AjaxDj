from django.shortcuts import render
from .forms import OfficeForm, EmployeeForm


def home(request):
    off_form = OfficeForm()
    emp_form = EmployeeForm()
    context = {
        'off_form': off_form,
        'emp_form': emp_form,
    }
    return render(request, 'emp_app/index.html', context=context)