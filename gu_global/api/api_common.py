from products.models import Category
from django.core.paginator import Paginator


# def get_common_context():
#     context_dict = {
#         'yealink_list':Category.objects.filter(main_category='Yealink').order_by('order'),
#         'sony_list':Category.objects.filter(main_category='SONY').order_by('order'),
#         'other_list':Category.objects.filter(main_category='Other').order_by('order')
#     }
#     return context_dict



def get_common_context(page_1=None, page_2=None, page_3=None, title=None, sub_title=None):

    banner_yealink = dict()
    yealink_list = Category.objects.filter(main_category='Yealink').order_by('order')
    for product in yealink_list:
        banner_yealink[product.name] = '/products/Yealink/{}'.format(product.name)

    banner_sony = dict()
    sony_list = Category.objects.filter(main_category='SONY').order_by('order')
    for product in sony_list:
        banner_sony[product.name] = '/products/SONY/{}'.format(product.name)
    
    banner_others = dict()
    other_list = Category.objects.filter(main_category='Other').order_by('order')
    for product in other_list:
        banner_others[product.name] = '/products/Other/{}'.format(product.name)

    banner_common = {
        'Company':'/company', 
        'Products':'/products/Yealink/{}'.format(yealink_list.first().name),
        'Solution':'/solution', 
        'Support':'/support', 
    }
    
    banner_company = {
        '회사소개':'/company', 
        '조직도':'/company/org', 
        '연혁':'/company/history', 
        '파트너사':'/company/partner', 
        '포트폴리오':'/company/portfolio', 
        'Contact Us':'/company/contact', 
    }

    banner_product = {
        'Yealink':'/products/Yealink/{}'.format(yealink_list.first().name),
        'Sony':'/products/SONY/{}'.format(sony_list.first().name),
        'Others':'/products/Other/{}'.format(other_list.first().name),
    }

    banner_solution = {
        '스탠다드 화상회의 (H.323/SIP)':'/solution/',
        '클라우드 화상회의':'/solution/ym',
        'MS Teams 화상회의':'/solution/ms',
        '구축형 화상회의':'/solution/yms',
        '스마트 강의':'/solution/sony',
    }

    banner_support = {
        '공지사항':'/support/',
        '인증서':'/support/certification',
        '다운로드 센터':'/support/download?type=전체',
        '동영상':'/support/video',
        '문의게시판':'/support/contact',
    }

    banner_partner = {
        '파트너사':'/company/partner?type=partner',
        '고객사':'/company/partner?type=customer',
        '시/정부기관':'/company/partner?type=government',
        '협력사':'/company/partner?type=cooperate',
    }

    banner_download = {
        '전체':'/support/download?type=전체',
        '코덱':'/support/download?type=코덱',
        '카메라':'/support/download?type=카메라',
        '스피커폰':'/support/download?type=스피커폰',
        '사용자 가이드':'/support/download?type=사용자 가이드',
        '소프트웨어':'/support/download?type=소프트웨어',
    }

    banner_dict = {
        'Company':banner_company,
        'Products':banner_product,
        'Solution':banner_solution,
        'Support':banner_support,
        
        '파트너사':banner_partner,
        'Yealink':banner_yealink,
        'SONY':banner_sony,
        'Other':banner_others,
        '다운로드 센터':banner_download,
    }

    context_dict = {
        'yealink_list':yealink_list,
        'sony_list':sony_list,
        'other_list':other_list,
        
        'banner_1': banner_common if page_1 else None,
        'banner_2': banner_dict[page_1] if page_2 else None,
        'banner_3': banner_dict[page_2] if page_3 else None,
        'current_page': [page_1, page_2, page_3],
        
        'title':title if title else page_1,
        'sub_title':sub_title if sub_title else page_2
    }
    return context_dict




def get_banner(page=None):

    yealink_list = Category.objects.filter(main_category='Yealink').order_by('order')

    banner_common = {
        'Company':'/company', 
        'Products':'/products/Yealink/{}'.format(yealink_list.first().name), 
        'Solution':'/solution', 
        'Support':'/support', 
    }
    
    banner_company = {
        '회사소개':'/company', 
        '조직도':'/company/org', 
        '연혁':'/company/history', 
        '파트너사':'/company/partner', 
        '포트폴리오':'/company/portfolio', 
        'Contact Us':'/company/contact', 
    }

    banner_partner = {
        '파트너사':'/company/partner?type=partner',
        '고객사':'/company/partner?type=customer',
        '시/정부기관':'/company/partner?type=government',
        '협력사':'/company/partner?type=cooperate',
    }

    banner_dict = {
        'common':banner_common,
        'company':banner_company,
        'partner':banner_partner
    }
    
    return banner_dict[page]


def get_paginated_list(request, list, item_per_page=10):

    page = request.GET.get('page', '1')
    paginator = Paginator(list, item_per_page)
    page_obj = paginator.page(page)

    current_page = page_obj.number
    min_num = max(1, current_page-2)
    max_num = min(current_page+3, paginator.num_pages+1)
    my_range  = range(min_num, max_num)

    return {'list':page_obj.object_list, 'page_obj':page_obj, 'my_range':my_range}