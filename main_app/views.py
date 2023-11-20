from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Car, Feature
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
    # get the features that the car doesn't have:
    # first, create the list of the feature ids that the car DOES ahve
    id_list = car.features.all().values_list('id')
    # now we can query for features whose ids are not in the list, using exclude()
    features_car_doesnt_have = Feature.objects.exclude(id__in=id_list)
    fueling_form = FuelingForm()
    return render(request, 'cars/detail.html', {
        'car': car, 
        'fueling_form': fueling_form, 
        # add the features to be displayed
        'features': features_car_doesnt_have
    })

class CarCreate(CreateView):
    model = Car
    fields = ['make', 'model', 'year', 'engine']
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

def assoc_feature(request, car_id, feature_id):
    # you CAN pass a feaute's id instead of the whole feature object
    Car.objects.get(id=car_id).features.add(feature_id)
    return redirect('detail', car_id = car_id )

def remove_feature(request, car_id, feature_id):
    # you CAN pass a feaute's id instead of the whole feature object
    Car.objects.get(id=car_id).features.remove(feature_id)
    return redirect('detail', car_id = car_id )

class FeatureList(ListView):
    model = Feature

class FeatureDetail(DetailView):
    model = Feature

class FeatureCreate(CreateView):
    model = Feature
    fields = '__all__'
    success_url = '/features'

class FeatureUpdate(UpdateView):
    model = Feature
    fields = '__all__'

class FeatureDelete(DeleteView):
    model = Feature
    success_url = '/features'