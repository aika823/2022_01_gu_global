from django.shortcuts import render

def vc(request):
    return render(request, "vc.html")

def ym(request):
    return render(request, "ym.html")