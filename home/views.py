from django.shortcuts import render
from home.models import Content
# Create your views here.


def home(request):
    data1, data2 = Content.objects.filter(category='Home')
    cards = Content.objects.filter(category='Card')
    # return render(request, 'home/home.html', {'home': data})
    return render(request, 'home/home.html', {'home1': data1, 'home2': data2, 'cards': cards})


def contact(request):
    return render(request, 'home/contact.html')


def about(request):
    message = Content.objects.get(pk=4)
    return render(request, 'home/about.html', {'data': message})


def principal(request):
    message = Content.objects.get(pk=1)
    return render(request, 'home/principal.html', {'data': message})


def administrator(request):
    message = Content.objects.get(pk=2)
    return render(request, 'home/administrator.html', {'data': message})


def president(request):
    message = Content.objects.get(pk=3)
    return render(request, 'home/president.html', {'data': message})
