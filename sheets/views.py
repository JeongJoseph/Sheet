# Create your views here.
from django.shortcuts import render
from models import Person
from os import path


def people(request) :
    return render(request,"people2.html",{"people":Person.objects.all()})