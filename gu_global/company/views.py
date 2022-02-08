from django.shortcuts import render
from api import api_common

def index(request):
    print('index')
    context = api_common.get_common_context()
    return render(request, "index.html", context=context)

def intro(request):
    context = api_common.get_common_context()
    return render(request, "intro.html", context=context)

def org(request):
    context = api_common.get_common_context()
    return render(request, "org.html", context=context)

def history(request):
    context = api_common.get_common_context()
    return render(request, "history.html", context=context)

def partner(request):
    context = api_common.get_common_context()
    return render(request, "partner.html", context=context)

def works(request):
    context = api_common.get_common_context()
    return render(request, "works.html", context=context)