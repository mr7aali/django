from django.shortcuts import render

from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Hey i want to free palestine")


def home(request):
    return render(request, "index.html")
