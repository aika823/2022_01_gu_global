from django.shortcuts import render
from api import api_common
from products.models import Product, Category, ProductDetailImage, ProductImage
from django.db.models import Q


def list(request):
    context = api_common.get_common_context('Products', 'Yealink')
    product_list = Product.objects.all()
    for product in product_list:
        try:
            thumbnail = ProductImage.objects.filter(product=product).first()
            product.thumbnail = thumbnail.image
        except:
            pass
    context['product_list'] = product_list    
    return render(request, "list.html", context=context)


def detail(request, id):
    context = api_common.get_common_context()
    product = Product.objects.get(id=id)
    image_list = ProductImage.objects.filter(product=product)
    detail_image_list = ProductDetailImage.objects.filter(product=product)
    update_context = {
        'product':product, 
        'thumbnail':image_list[0],
        'image_list':image_list[1:], 
        'detail_image_list':detail_image_list,
    }
    context.update(update_context)
    return render(request, "detail.html", context=context)


def category_list(request, main_category, category_name=None):

    context = api_common.get_common_context('Products', main_category, category_name)
    category = Category.objects.get(name=category_name)
    product_list = Product.objects.filter(category=category)

    has_sub_category = False
    for product in product_list:
        if product.sub_category:
            has_sub_category = True
            break
    
    if request.GET.get('주변기기') == 'True':
        product_list = Product.objects.filter(Q(category=category) & Q(sub_category='주변기기'))
        sub_active = [None, 'active']
    else:
        product_list = Product.objects.filter(Q(category=category) & ~Q(sub_category='주변기기'))
        sub_active = ['active', None]
    
    print(product_list.query)

    for product in product_list:
        print(product.name)


        
    for product in product_list:
        try:
            thumbnail = ProductImage.objects.filter(product=product).first()
            product.thumbnail = thumbnail.image
        except:
            pass
    
    context['product_list'] = product_list
    context['has_sub_category'] = has_sub_category
    context['sub_active'] = sub_active
    return render(request, "list.html", context=context)