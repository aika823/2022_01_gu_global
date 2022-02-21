from products.models import Category
from django.core.paginator import Paginator


# def get_common_context():
#     context_dict = {
#         'yealink_list':Category.objects.filter(main_category='Yealink').order_by('order'),
#         'sony_list':Category.objects.filter(main_category='SONY').order_by('order'),
#         'other_list':Category.objects.filter(main_category='Other').order_by('order')
#     }
#     return context_dict



def get_common_context(page_1=None, page_2=None, page_3=None):


    banner_common = {
        'Company':'/company', 
        'Products':'/product', 
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
        'Yealink':'/products/Yealink',
        'Sony':'/products/Sony',
        'Others':'/products/Others',
    }

    banner_partner = {
        '파트너사':'/company/partner?type=partner',
        '고객사':'/company/partner?type=customer',
        '시/정부기관':'/company/partner?type=government',
        '협력사':'/company/partner?type=cooperate',
    }

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


    banner_dict = {
        'company':banner_company,
        'Products':banner_product,
        
        'partner':banner_partner,
        'Yealink':banner_yealink,
        'SONY':banner_sony,
        'Other':banner_others,
    }


    context_dict = {
        'yealink_list':yealink_list,
        'sony_list':Category.objects.filter(main_category='SONY').order_by('order'),
        'other_list':other_list,
        'banner_1': banner_common if page_1 else None,
        'banner_2': banner_dict[page_1] if page_2 else None,
        'banner_3': banner_dict[page_2] if page_3 else None,
        'current_page': [page_1, page_2, page_3]

    }
    return context_dict




def get_banner(page=None):

    banner_common = {
        'Company':'/company', 
        'Products':'/product', 
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

    banner_products = {
        'Yealink':'/products/Sony',
        'Sony':'/products/Sony',
        'Sony':'/products/Sony',
        
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
    return {'list':page_obj.object_list, 'page_obj':page_obj}