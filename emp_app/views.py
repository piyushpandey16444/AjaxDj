from django.shortcuts import render
from .forms import OfficeForm, EmployeeForm
from django.views.decorators.csrf import csrf_exempt


def home(request):
    off_form = OfficeForm()
    emp_form = EmployeeForm()
    context = {
        'off_form': off_form,
        'emp_form': emp_form,
    }
    return render(request, 'emp_app/index.html', context=context)

@csrf_exempt
def create_off_view(request):
    print("request.POST: ", request.POST)
    print("request.body: ", request.body)
