from django.shortcuts import render
from api import api_common
from products.models import BestProduct
from support.models import Contact, Notice, Popup
from datetime import date
from django.contrib.auth.hashers import make_password
# Send Email
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.core import mail
from django.core.mail import EmailMessage



def index(request):
    context = api_common.get_common_context('Company')
    context['notice_list'] = Notice.objects.all().order_by('-date')[:3]
    context['best_product_list'] = BestProduct.objects.all().order_by('order')
    today = date.today()
    
    popup_list = list()
    for popup in Popup.objects.all():
        if popup.start < today < popup.end :
            popup_list.append(popup)
            
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

def location(request):
    context = api_common.get_common_context('Company','Location')
    return render(request, "location.html", context=context)

def contact(request):
    if request.method == 'POST':

        email = request.POST.get('email')
        title = request.POST.get('title')
        content = request.POST.get('content')
        type = request.POST.get('type')
        file = request.FILES.get('file')
        
        # Save Data
        contact = Contact()
        contact.email = email
        contact.title = title
        contact.content = content
        contact.type = type
        contact.password = make_password(request.POST.get('password'))
        contact.file = file
        contact.save()
        
        # Send Email
        admin_email = "aika823@naver.com"
        html_message = render_to_string('email.html', {'content':content,'contact':contact})
        plain_message = strip_tags(html_message)

        email_body = """\
            <html>
            <head></head>
            <body>
                <p>{}</p>
                <br>
                <a href="https://guglobal.gabia.io/admin/contact/{}">관리자 페이지에서 확인하기</a>
            </body>
            </html>
        """.format(contact.title, contact.content, contact.id)

        email_message = EmailMessage(
            subject="[{}] {}".format(type, title),
            body=email_body,
            from_email='GU GLOBAL',
            to=[admin_email],
            reply_to=[email],
        )
        email_message.content_subtype = "html"
        if contact.file:
            email_message.attach_file(str(contact.file))
        email_message.send()
    
    context = api_common.get_common_context('Company','문의하기')
    return render(request, "contact_page.html", context=context)