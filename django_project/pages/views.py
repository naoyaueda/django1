from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})

def school_view(request, *args, **kwargs):
    return render(request, "school.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})
