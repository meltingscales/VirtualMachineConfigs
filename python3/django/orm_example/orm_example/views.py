from django.http import HttpResponse
from django.shortcuts import render

from orm_example.models import PersonForm


def index(request):
    return HttpResponse('<p>Hello! I am the index.</p>'
                        '<ul>'
                        '<li><a href="new_person">new person</a></li>'
                        '</ul>')


def new_person(request):
    return render(request, "person.html", context={"form": PersonForm})
