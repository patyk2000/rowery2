from multiprocessing import context
from tempfile import _TemporaryFileWrapper
from django.shortcuts import render
from .models import Typeofbike, Parts, Bike
from rowery2.forms import Form

def index(request):
    index_list = Bike.objects.all()
    context = {'index_list': index_list}
    return render(request, 'rowery2/index.html', context)

def typeofbike(request):
    type_list = Typeofbike.objects.all
    context = {'types_list':type_list}
    return render(request, 'rowery2/typeofbike.html')

def parts(request):
    parts_list = Parts.objects.all
    context = {'parts_list':parts_list}
    return render(request, 'rowery2/parts.html')

def bike(request):
    bike_list = Bike.objects.all
    context = {'bike_list':bike_list}
    return render(request, 'rowery2/bike.html') 

def form(request):
    form_list = Form(request.POST or None)
    if form_list.is_valid():
        form_list.save() #sprawdza czy są zmiany
    context = {'form':form_list}
    return render(request,'rowery2/form.html', context)