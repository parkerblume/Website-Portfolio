from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic.base import TemplateView


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")


def projects(request: HttpRequest) -> HttpResponse:
    return render(request, "projects.html")
