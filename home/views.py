from django.shortcuts import render

from django.http import HttpResponse


# def home(request):
#     return HttpResponse("Hey i want to free palestine")
def home(request):
    peoples = [
        {"name":"Sheikh Ali", "age":50},
        {"name":"Mr ali", "age":52},
        {"name":"my name is lai", "age":59},
        {"name":"Fardin khan", "age":10},
    ]
    return render(request, "index.html", context={"peoples":peoples})
