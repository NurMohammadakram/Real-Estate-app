from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'real_estate/about.html')

def contact(request):
    return render(request, 'real_estate/contact.html')

def for_sale(request):
    return render(request, 'real_estate/for_sale.html')

def rent(request):
    return render(request, 'real_estate/rent.html')

def properties(request):
    return render(request, 'real_estate/properties.html')

@login_required
def owners(request):
    if request.user.profile.role != 'owner':
        return render(request, 'real_estate/owners.html')
    
    return render(request, 'owner/dashboard.html')