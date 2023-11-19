from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car
from .forms import FuelingForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {'cars': cars})

def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    fueling_form = FuelingForm()
    return render(request, 'cars/detail.html', {'car': car, 'fueling_form': fueling_form})

class CarCreate(CreateView):
    model = Car
    fields = '__all__'
    # success_url = '/cars/{car_id}'

class CarUpdate(UpdateView):
    model = Car
    fields = ['year', 'engine']

class CarDelete(DeleteView):
    model = Car
    success_url = '/cars'

def add_fueling(request, car_id):
# create a ModelForm instance using the data in request.POST
  form = FuelingForm(request.POST)
# validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the car_id assigned
    new_fueling = form.save(commit=False)
    new_fueling.car_id = car_id
    new_fueling.save()
  return redirect('detail', car_id=car_id) 
