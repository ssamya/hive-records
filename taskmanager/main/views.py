from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def eq(request):
    return render(request, 'main/eq.html')


def pricing(request):
    return render(request, 'main/pricing.html')


def faqs(request):
    return render(request, 'main/faqs.html')
