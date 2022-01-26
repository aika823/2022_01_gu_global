from django.shortcuts import render

def index(request):
    print('index')
    return render(request, "index.html")

def intro(request):
    return render(request, "intro.html")
