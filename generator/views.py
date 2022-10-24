from django.shortcuts import render
import random

# Create your views here.

def home(request):
    title = 'Generator'
    return render(request, 'generator/home.html', {'title':title})


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    length = int(request.GET.get('length', 10))
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!"№;%:?*()'))

    if request.GET.get('number'):
        characters.extend(list('012345789'))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    title = 'Password generation'

    return render(request, 'generator/password.html', {'password':thepassword, 'title':title})

def about(request):
    title = 'About'
    return render(request, 'generator/about.html', {'title': title})
