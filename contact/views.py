from django.http import HttpResponse, FileResponse, Http404
from django.shortcuts import render


def index(request):
    try:
        context = {}
        return render(request, 'contact.html', context)

    except FileNotFoundError:
        raise Http404()
