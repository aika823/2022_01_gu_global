from django.shortcuts import render
from api import api_common
from support.models import Contact

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

def portfolio(request):
    context = api_common.get_common_context()
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
        print(request.FILES)
        print(request.FILES.get('file'))
        contact.save()
    context = api_common.get_common_context()
    return render(request, "contact_page.html", context=context)