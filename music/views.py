from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h3>The music app homepage</h3>")


def detail(request, id):
    return HttpResponse("<h2>Details for Album id:" + str(id) + "</h2>")