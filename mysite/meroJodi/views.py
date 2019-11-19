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
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView

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
class RegisterView(CreateView):
    template_name = "register.html"

    def post(self, request):
        form = ProfileRegisterFormOne(request.POST)
        print(form.as_table)
        if form.is_valid():
            form.save()
            return redirect('register_two')
        return render(request, template_name, {'form': form})

    def get(self, request):
        form = ProfileRegisterFormOne()
        return render(request, 'register.html', {'form': form})


class RegisterViewTwo(UpdateView):
    def post(self, request):
        form = ProfileRegisterFormTwo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_three')
        return render(request, 'register_two.html', {'form': form})

    def get(self, request):
        form = ProfileRegisterFormTwo()
        return render(request, 'register_two.html', {'form': form})


class RegisterViewThree(UpdateView):
    def post(self, request):
        form = ProfileRegisterFormThree(request.POST)
        if form.is_valid():
            form.save()
            return redirect('firstpage')
        return render(request, 'register_three.html', {'form': form})

    def get(self, request):
        form = ProfileRegisterFormThree()
        return render(request, 'register_three.html', {'form': form})
    # ======> Registration End <==========


def firstpage_view(request):
    return render(request, "meroJodi/login/firstpage.html", {})


def profiles_view(request):
    return render(request, "meroJodi/login/profiles.html", {})
