from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from Travel_Application.forms import TravelForm, ContactForm
from Travel_Application.models import Travel, TouristGuide
from datetime import datetime
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    guides = Travel.objects.all()
    return render(request, 'index.html', context={'guides': guides})

def add_travel(request):
    if request.method == 'POST':
        form = TravelForm(request.POST, request.FILES)
        if form.is_valid():
            travel = form.save(commit=False)
            travel.touristGuide = TouristGuide.objects.filter(user=request.user).first()
            travel.save()

        return redirect('index')

    form = TravelForm()
    return render(request, 'add_travel.html', context={'form': form})

def edit_travel(request, travel_id):
    travel = get_object_or_404(Travel, pk=travel_id)
    # Flight.objects.filter(pk=flight_id).exists()

    if request.method == 'POST':
        form = TravelForm(request.POST, request.FILES, instance=travel)
        if form.is_valid():
            form.save()

        return redirect('index')

    form = TravelForm(instance=travel)
    return render(request, "edit_travel.html", context={'form': form, 'travel_id': travel_id})

@login_required
def delete_travel(request, travel_id):
    travel = get_object_or_404(Travel, pk=travel_id)

    if travel.touristGuide.user == request.user:
        travel.delete()

    return redirect('index')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass
        return redirect('index')

    form = ContactForm()
    return render(request, "contact.html", context={'form': form})


def details(request, travel_id):
    travel = Travel.objects.filter(id=travel_id).first()
    context = {'travel_data': travel, 'app_name': 'Travel_Application'}
    return render(request, 'details.html', context)