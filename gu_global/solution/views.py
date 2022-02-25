from django.shortcuts import render
from api import api_common

def vc(request):
    context = api_common.get_common_context('Solution','VC')
    context['solution_name'] = request.GET.get('name')
    return render(request, "vc.html", context=context)


def ms(request):
    context = api_common.get_common_context('Solution','MS')
    context['solution_name'] = request.GET.get('name')
    return render(request, "ms.html", context=context)


def yms(request):
    context = api_common.get_common_context('Solution','YMS')
    context['solution_name'] = request.GET.get('name')
    return render(request, "yms.html", context=context)


def ym(request):
    context = api_common.get_common_context('Solution','YM')
    context['solution_name'] = request.GET.get('name')
    return render(request, "ym.html", context=context)


def sony(request):
    context = api_common.get_common_context('Solution','SONY')
    context['solution_name'] = request.GET.get('name')
    return render(request, "sony.html", context=context)