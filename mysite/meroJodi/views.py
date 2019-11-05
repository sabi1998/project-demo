from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index_view(request):
    return render(request, "meroJodi/index.html", {})


def login_view(request):
    return render(request, "meroJodi/login.html", {})


def register_view(request):
    return render(request, "meroJodi/register.html", {})


def register_two_view(request):
    return render(request, "meroJodi/register2.html", {})


def register_three_view(request):
    return render(request, "meroJodi/register3.html", {})


def firstpage_view(request):
    return render(request, "meroJodi/firstpage.html", {})


def profiles_view(request):
    return render(request, "meroJodi/profiles.html", {})
