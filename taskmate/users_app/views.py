from django.shortcuts import render
# from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


def register(request):
    # return HttpResponse("users_app working!")
    register_form = UserCreationForm()
    return render(request, 'register.html', {'register_form': register_form})
