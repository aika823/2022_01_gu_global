from itertools import product
from multiprocessing import context
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.hashers import make_password, check_password

from products.models import Product
from .models import Contact, Notice, Video
from api.api_common import get_paginated_list, get_common_context



def notice(request):
  notice_list = Notice.objects.all().order_by('-date')
  # 역순 카운트
  i=0
  for notice in notice_list:
        notice.number = notice_list.count()-i
        i = i+1
  context = get_common_context('Support','공지사항')
  context['notice_list'] = get_paginated_list(request, notice_list)['list']
  context['page_obj'] = get_paginated_list(request, notice_list)['page_obj']
  context['my_range'] = get_paginated_list(request, notice_list)['my_range']
  context['total_count'] = notice_list.count()
  return render(request, 'support_notice.html', context=context)


def notice_more(request, id):
  notice = Notice.objects.get(id=id)
  context = get_common_context('Support','공지사항')
  context['notice'] = notice
  notice.views = notice.views + 1
  notice.save()
  return render(request, 'notice_more.html', context=context) 


# def certification(request):
#   context = get_common_context('Support','인증서')
#   return render(request, "certification.html", context=context)


def download(request):
      
  product_list = Product.objects.all()
  
  active_dict ={
    'codec':'active' if request.GET.get('type') == '코덱' else '',
    'camera':'active' if request.GET.get('type') == '카메라' else '',
    'speaker_phone':'active' if request.GET.get('type') == '스피커폰' else '',
    'guide':'active' if request.GET.get('type') == '사용자 가이드' else '',
    'software':'active' if request.GET.get('type') == '소프트웨어' else '',
  }

  selected_dict ={
    'codec':'selected' if request.GET.get('type') == '코덱' else '',
    'camera':'selected' if request.GET.get('type') == '카메라' else '',
    'speaker_phone':'selected' if request.GET.get('type') == '스피커폰' else '',
    'guide':'selected' if request.GET.get('type') == '사용자 가이드' else '',
    'software':'selected' if request.GET.get('type') == '소프트웨어' else '',
  }

  type_dict = {
    '코덱':'codec',
    '카메라':'camera',
    '스피커폰':'speaker_phone',
    '사용자 가이드':'guide',
    '소프트웨어':'software',
  }  

  type = request.GET.get('type') if request.GET.get('type') else None
  keyword = request.GET.get('keyword') if request.GET.get('keyword') else None

  if type and type not in ['전체', 'all']:
    product_list = product_list.filter(type=type_dict[type])
  else:
    active_dict = None
  
  if keyword:
      product_list = product_list.filter(name__icontains=keyword)
    
  
  # 역순 카운트
  i=0
  for product in product_list:
        product.number = product_list.count()-i
        i = i+1
        
    
  context = get_common_context('Support','다운로드 센터', type)
  context['product_list'] = get_paginated_list(request, product_list)['list']
  context['page_obj'] = get_paginated_list(request, product_list)['page_obj']
  context['my_range'] = get_paginated_list(request, product_list)['my_range']
  context['active'] = active_dict
  context['selected'] = selected_dict
  context['keyword'] = keyword
  context['total_count'] = product_list.count()
  
  return render(request, "support_download.html", context=context)


def video(request):
    video_list = Video.objects.all()  
    context = get_common_context('Support','동영상')
    # context['video_list'] = video_list
    context['video_list'] = get_paginated_list(request, video_list)['list']
    context['page_obj'] = get_paginated_list(request, video_list)['page_obj']
    context['my_range'] = get_paginated_list(request, video_list)['my_range']
    return render(request, "support_video.html", context=context)


def contact(request):
  contact_list = Contact.objects.all()
  context = get_common_context('Support','문의하기')
  context['contact_list'] = get_paginated_list(request, contact_list)['list']
  context['page_obj'] = get_paginated_list(request, contact_list)['page_obj'] 
  context['my_range'] = get_paginated_list(request, contact_list)['my_range'] 
  
  if request.POST.get('id') and request.POST.get('password'):
        contact = Contact.objects.get(id=request.POST.get('id'))
        if check_password(request.POST.get('password'), contact.password):
              print('good')
              request.session['contact_id'] = request.POST.get('id')
              return redirect('/support/contact/{}'.format(request.POST.get('id')))

  
  return render(request, "support_contact.html", context=context)


def contact_more(request, id):

      if str(request.session.get('contact_id')) == str(id):
            contact_list = Contact.objects.all()
            contact = Contact.objects.get(id=id)
            if contact.file:
              contact.new_file_name = str(contact.file)[14:]
            context = get_common_context('Support','문의하기')
            context['contact'] = contact
            context['contact_list'] = get_paginated_list(request, contact_list)['list']
            context['page_obj'] = get_paginated_list(request, contact_list)['page_obj'] 
            context['my_range'] = get_paginated_list(request, contact_list)['my_range'] 
            return render(request, "contact_more.html", context=context)
      else:
            print("bad")
            return redirect("/support/contact")
  


def contact_form(request):
  
  if request.method == 'POST':
        contact = Contact()
        contact.type = request.POST.get('type')
        contact.title = request.POST.get('title')
        contact.email = request.POST.get('email')
        contact.content = request.POST.get('content')
        contact.password = make_password(request.POST.get('password'))
        contact.file = request.FILES.get('file')
        contact.save()

  contact_list = Contact.objects.all()
  context = get_common_context('Support','문의하기')
  context['contact_list'] = get_paginated_list(request, contact_list)['list']
  context['page_obj'] = get_paginated_list(request, contact_list)['page_obj'] 
  context['my_range'] = get_paginated_list(request, contact_list)['my_range'] 
  return render(request, "contact_form.html", context=context)