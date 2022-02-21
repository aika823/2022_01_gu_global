from itertools import product
from multiprocessing import context
from django.shortcuts import render
from django.core.paginator import Paginator

from products.models import Product
from .models import Contact, Notice, Video
from api.api_common import get_paginated_list, get_common_context


def notice(request):
  notice_list = Notice.objects.all()
  context = get_common_context('Support','공지사항')
  context['notice_list'] = get_paginated_list(request, notice_list)['list']
  context['page_obj'] = get_paginated_list(request, notice_list)['page_obj']
  return render(request, 'support_notice.html', context=context) 


def certification(request):
  context = get_common_context('Support','인증서')
  return render(request, "certification.html", context=context)


def download(request):
      
  product_list = Product.objects.all()
  
  active_dict ={
    'codec':'active' if request.GET.get('type') == '코덱' else '',
    'camera':'active' if request.GET.get('type') == '카메라' else '',
    'speaker_phone':'active' if request.GET.get('type') == '스피커폰' else '',
    'guide':'active' if request.GET.get('type') == '사용자 가이드' else '',
    'software':'active' if request.GET.get('type') == '소프트웨어' else '',
  }

  type_dict = {
    '코덱':'codec',
    '카메라':'camera',
    '스피커폰':'speaker_phone',
    '사용자 가이드':'guide',
    '소프트웨어':'software',
  }  

  if request.GET.get('type'):
        if request.GET.get('type') == '전체':
              active_dict = None
        else:
              product_list = product_list.filter(type=type_dict[request.GET.get('type')])
  
  if request.GET.get('keyword'):
        product_list = product_list.filter(title__contains=request.GET.get('keyword'))
    
  context = get_common_context('Support','다운로드 센터', request.GET.get('type'))
  context['product_list'] = get_paginated_list(request, product_list)['list']
  context['page_obj'] = get_paginated_list(request, product_list)['page_obj']
  context['active'] = active_dict
  
  return render(request, "support_download.html", context=context)


def video(request):
    video_list = Video.objects.all()  
    context = get_common_context('Support','동영상')
    # context['video_list'] = video_list
    context['video_list'] = get_paginated_list(request, video_list)['list']
    context['page_obj'] = get_paginated_list(request, video_list)['page_obj']
    return render(request, "support_video.html", context=context)


def contact(request):
  contact_list = Contact.objects.all()
  context = get_common_context('Support','문의게시판')
  context['contact_list'] = get_paginated_list(request, contact_list)['list']
  context['page_obj'] = get_paginated_list(request, contact_list)['page_obj'] 
  return render(request, "support_contact.html", context=context)