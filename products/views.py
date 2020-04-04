from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello fuckers")


def newPage(request):
    return HttpResponse("Hitting the new view route")

