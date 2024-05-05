from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'title': 'Home Page',
        'content': 'This is the home page',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'is_authenticater': True
    }
    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse("About Page")
