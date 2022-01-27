from django.shortcuts import render

def index(request):
    print('index')
    return render(request, "index.html")

def intro(request):
    return render(request, "intro.html")

def org(request):
    return render(request, "org.html")

def history(request):
    return render(request, "history.html")

def partner(request):
    return render(request, "partner.html")

def works(request):
    return render(request, "works.html")