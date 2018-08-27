from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render


def index(request):
    try:
        context = {}
        return render(request, 'personalSite/resume.html', context)
    except FileNotFoundError:
        raise Http404()
