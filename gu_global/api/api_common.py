from products.models import Category
from django.core.paginator import Paginator


def get_common_context():
    context_dict = {
        'yealink_list':Category.objects.filter(main_category='Yealink').order_by('order'),
        'sony_list':Category.objects.filter(main_category='SONY').order_by('order'),
        'other_list':Category.objects.filter(main_category='Other').order_by('order')
    }
    return context_dict


def get_paginated_list(request, list, item_per_page=10):
    page = request.GET.get('page', '1')
    paginator = Paginator(list, item_per_page)
    page_obj = paginator.page(page)
    return {'list':page_obj.object_list, 'page_obj':page_obj}