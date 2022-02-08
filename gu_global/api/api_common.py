from products.models import Category

def get_common_context():
    context_dict = {
        'yealink_list':Category.objects.filter(main_category='Yealink').order_by('order'),
        'sony_list':Category.objects.filter(main_category='SONY').order_by('order'),
        'other_list':Category.objects.filter(main_category='Other').order_by('order')
    }
    return context_dict