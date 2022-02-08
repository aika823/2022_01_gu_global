from django.shortcuts import render
from api import api_common

def vc(request):
    context = api_common.get_common_context()
    return render(request, "vc.html", context=context)

def ym(request):
    context = api_common.get_common_context()
    return render(request, "ym.html", context=context)