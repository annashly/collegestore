from django.shortcuts import render
from .models import Department


# Create your views here.
def index(request):
    obj = Department.objects.all()
    return render(request,"index.html",{'result':obj})


# Create your views here.
