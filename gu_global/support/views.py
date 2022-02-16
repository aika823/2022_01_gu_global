from itertools import product
from multiprocessing import context
from django.shortcuts import render
from django.core.paginator import Paginator

from products.models import Product
from .models import Contact, Notice, Video
from api.api_common import get_paginated_list, get_common_context


def notice(request):
  notice_list = Notice.objects.all()
  context = get_common_context()
  context['notice_list'] = get_paginated_list(request, notice_list)['list']
  context['page_obj'] = get_paginated_list(request, notice_list)['page_obj']
  return render(request, 'support_notice.html', context=context) 


def certification(request):
  context = get_common_context()
  return render(request, "certification.html", context=context)


def download(request):
      
  product_list = Product.objects.all()
  
  active_dict ={
    'codec':'active' if request.GET.get('type') == 'codec' else '',
    'camera':'active' if request.GET.get('type') == 'camera' else '',
    'speaker_phone':'active' if request.GET.get('type') == 'speaker_phone' else '',
    'guide':'active' if request.GET.get('type') == 'guide' else '',
    'software':'active' if request.GET.get('type') == 'software' else '',
  }

  if request.GET.get('type'):
        if request.GET.get('type') == 'all':
              active_dict = None
        else:
              product_list = product_list.filter(type=request.GET.get('type'))
  
  if request.GET.get('keyword'):
        product_list = product_list.filter(title__contains=request.GET.get('keyword'))

  context = get_common_context()
  context['product_list'] = get_paginated_list(request, product_list)['list']
  context['page_obj'] = get_paginated_list(request, product_list)['page_obj']
  context['active'] = active_dict
  
  return render(request, "support_download.html", context=context)


def video(request):
    video_list = Video.objects.all()  
    context = get_common_context()
    context['video_list'] = video_list
    return render(request, "support_video.html", context=context)


def contact(request):
  contact_list = Contact.objects.all()
  context = get_common_context()
  context['contact_list'] = get_paginated_list(request, contact_list)['list']
  context['page_obj'] = get_paginated_list(request, contact_list)['page_obj'] 
  return render(request, "support_contact.html", context=context)