from django.shortcuts import render
from api import api_common

def vc(request):
    context = api_common.get_common_context()
    return render(request, "vc.html", context=context)


def ms(request):
    context = api_common.get_common_context()
    return render(request, "ms.html", context=context)


def yms(request):
    context = api_common.get_common_context()
    return render(request, "yms.html", context=context)


def ym(request):
    context = api_common.get_common_context()
    return render(request, "ym.html", context=context)


def sony(request):
    context = api_common.get_common_context()
    return render(request, "sony.html", context=context)