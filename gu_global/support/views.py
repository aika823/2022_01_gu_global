from itertools import product
from multiprocessing import context
from django.shortcuts import render
from django.core.paginator import Paginator

from products.models import Product
from .models import Contact, Notice, Video
from api.api_common import get_paginated_list


def notice(request):
  notice_list = Notice.objects.all()
  context = {
    'notice_list':get_paginated_list(request, notice_list)['list'],
    'page_obj':get_paginated_list(request, notice_list)['page_obj'] 
  }
  return render(request, 'support_notice.html', context=context) 


def certification(request):
  return render(request, "certification.html")


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

  context = {
    'product_list':get_paginated_list(request, product_list)['list'],
    'page_obj':get_paginated_list(request, product_list)['page_obj'],
    'active' :active_dict
  }
  return render(request, "support_download.html", context=context)


def video(request):
    video_list = Video.objects.all()  
    context = {
      'video_list':video_list
    }
    return render(request, "support_video.html", context=context)


def contact(request):
  contact_list = Contact.objects.all()
  context = {
    'contact_list':get_paginated_list(request, contact_list)['list'],
    'page_obj':get_paginated_list(request, contact_list)['page_obj'] 
  }
  return render(request, "support_contact.html", context=context)


def test(request):
    board_list = Notice.objects.all() #models.py Board 클래스의 모든 객체를 board_list에 담음
    print(board_list)
    # board_list 페이징 처리
    page = request.GET.get('page', '1') # GET 방식으로 정보를 받아오는 데이터
    paginator = Paginator(board_list, '1') # 페이지 당 담길 객체 수
    page_obj = paginator.page(page) # 페이지 번호를 받아 해당 페이지를 리턴 get_page 권장
    return render(request, 'test.html', {'page_obj':page_obj}) 
