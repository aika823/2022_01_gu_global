from django.shortcuts import render
from api import api_common

def vc(request):
    context = api_common.get_common_context('Solution','스탠다드 화상회의')
    context['solution_name'] = request.GET.get('name')
    return render(request, "vc.html", context=context)


def ms(request):
    context = api_common.get_common_context('Solution','MS Teams 화상회의')
    context['solution_name'] = request.GET.get('name')
    return render(request, "ms.html", context=context)


def yms(request):
    context = api_common.get_common_context('Solution','구축형 화상회의')
    context['solution_name'] = request.GET.get('name')
    return render(request, "yms.html", context=context)


def ym(request):
    context = api_common.get_common_context('Solution','클라우드 화상회의')
    context['solution_name'] = request.GET.get('name')
    return render(request, "ym.html", context=context)


def sony(request):
    context = api_common.get_common_context('Solution','스마트 강의')
    context['solution_name'] = request.GET.get('name')
    return render(request, "sony.html", context=context)