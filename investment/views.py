from django.shortcuts import render, redirect
from .forms import InvestorForm, SignatoryForm, InstitutionForm
from .models import Investor, Institution

# Create your views here.
def home(request):
    investors = Investor.objects.all()
    institutions = Institution.objects.all()
    return render(request, 'investment/index.html', {'investors' : investors, 'institutions' : institutions})

def add_investor(request):
    form = InvestorForm()
    if request.method == 'POST':
        form = InvestorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'investment/add_investor.html', {"form":form})

# Create your views here.
def add_institution(request):
    form = InstitutionForm()
    if request.method == 'POST':
        form = InstitutionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'investment/add_institution.html', {"form":form})