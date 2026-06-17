from django.http import HttpResponse
from django.shortcuts import render


def homepage(request): 
    # return HttpResponse("Hello from home page")
    return render(request, 'index.html')