from django.shortcuts import render
from .models import Project 


def one(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/onee.html', {'projects':projects})
