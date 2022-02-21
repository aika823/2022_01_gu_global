from django.shortcuts import render
from api import api_common
from support.models import Contact, Notice, Popup
from datetime import date


def index(request):
    context = api_common.get_common_context()
    context['notice_list'] = Notice.objects.all().order_by('order')[:3]
    today = date.today()
    
    popup_list = list()
    for popup in Popup.objects.all():
        if popup.start < today < popup.end :
            popup_list.append(popup)
    
    print(popup_list)
            
    context['popup_list'] = popup_list[:1]
    return render(request, "index.html", context=context)


def intro(request):
    context = api_common.get_common_context('Company', '회사소개')
    return render(request, "intro.html", context=context)


def org(request):
    context = api_common.get_common_context('Company', '조직도')
    return render(request, "org.html", context=context)


def history(request):
    context = api_common.get_common_context('Company','연혁')
    return render(request, "history.html", context=context)


def partner(request):
    context = api_common.get_common_context('Company','파트너사','파트너사')
    return render(request, "partner.html", context=context)


def works(request):
    context = api_common.get_common_context()
    return render(request, "works.html", context=context)


def portfolio(request):
    context = api_common.get_common_context('Company','포트폴리오')
    return render(request, "portfolio.html", context=context)


def contact(request):
    if request.method == 'POST':
        contact = Contact()
        contact.type = request.POST.get('type')
        contact.title = request.POST.get('title')
        contact.email = request.POST.get('email')
        contact.content = request.POST.get('content')
        contact.password = request.POST.get('password')
        contact.file = request.FILES.get('file')
        contact.save()
    
    context = api_common.get_common_context('Company','Contact Us')
    return render(request, "contact_page.html", context=context)