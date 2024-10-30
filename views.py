# itsofolio/views.py
from django.shortcuts import render # type: ignore

def homepage(request):
    return render(request, 'homepage.html')  # Ensure this file exists in the templates directory
