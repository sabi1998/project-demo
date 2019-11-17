from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages
from .forms import *
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

# Create your views here.


def index_view(request):
    content = {}
    return render(request, "meroJodi/index.html", content)


@login_required
def special(request):
    return HttpResponse("You are logged in !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
# ======> Login Start <======


def login_view(request):
    return render(request, "meroJodi/registration/login.html", {})

# ======> Login End <======

# ======> Registration Start <==========


# @csrf_protect
def register_view(request):
    if request.method == 'POST':
        form1 = ProfileRegisterFormOne(request.POST)
        print("request is post ", request.method)
        if form1.is_valid():
            print("form1 is valid")
            register = form1.save(commit=False)
            # print("register", register.save())
            return register_two_view(request)
            # register.save()
            # register.save()

            # return HttpResponseRedirect(reverse('register_two'))
        else:
            print("form1 isnot valid")
            print(form1.errors)

    else:
        print("request is not post")
        form1 = ProfileRegisterFormOne()

    return render(request, "meroJodi/registration/register.html", {'form1': form1})


def register_two_view(request):
    if request.method == 'POST':
        form2 = ProfileRegisterFormTwo(request.POST)
        form1 = ProfileRegisterFormOne(request.POST)
        print("request is post ", request.method)
        if form2.is_valid():
            print("form2 is valid")
            register2 = form2.save(commit=False)
            return register_three_view(request)
            # form1.save()
            # register2.save()
            # return HttpResponseRedirect(reverse('firstpage'))
        else:
            print("form2 isnot valid")
            print(form2.errors)
    else:
        form2 = ProfileRegisterFormTwo()
        form1 = ProfileRegisterFormOne()
        print(form2.errors)
        print("form2 not a post request")
    return render(request, "meroJodi/registration/register2.html", {'form2': form2})


def register_three_view(request):
    if request.method == 'POST':
        form3 = ProfileRegisterFormThree(request.POST)
        form2 = ProfileRegisterFormTwo(request.POST)
        form1 = ProfileRegisterFormOne(request.POST)
        if form3.is_valid() and form2.is_valid() and form1.is_valid():
            register3 = form3.save(commit=False)
            register3.save()
            form2.save()
            form1.save()
            return HttpResponseRedirect(reverse('firstpage'))
        else:
            print("form3 isnot valid")
            print(form3.errors)
    else:
        form = ProfileRegisterFormThree()
        print("not a post request in form3")
    return render(request, "meroJodi/registration/register3.html", {'form3': form3})


# def registration(form):
#     print("registration")

    # ======> Registration End <==========


def firstpage_view(request):
    return render(request, "meroJodi/login/firstpage.html", {})


def profiles_view(request):
    return render(request, "meroJodi/login/profiles.html", {})
