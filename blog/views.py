from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
#     return HttpResponse('Hello World!')


def index(request):
    return render(request, 'blog/index.html', {'hello': 'Hello Blog ....'})
