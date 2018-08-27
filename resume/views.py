from django.http import HttpResponse, FileResponse, Http404
from django.shortcuts import render


def index(request):
    try:
        context = {}
        return render(request, 'resume.html', context)

    except FileNotFoundError:
        raise Http404()


def pdf(request):
    try:
        return FileResponse(open('/home/matt/git/personalSite/resume/Matthew_McLeod.pdf', 'rb'),
                            content_type='application/pdf')

    except FileNotFoundError:
        raise Http404()