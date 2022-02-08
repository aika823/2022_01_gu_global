from django.shortcuts import render
from api import api_common
from support.models import Download
from products.models import Product, Category, ProductDetailImage, ProductImage

def list(request):
    context = api_common.get_common_context()
    product_list = Product.objects.all()
    for product in product_list:
        thumbnail = ProductImage.objects.filter(product=product).first()
        product.thumbnail = thumbnail.image
    context['product_list'] = product_list    
    return render(request, "list.html", context=context)

def detail(request, product_name):
    context = api_common.get_common_context()
    product = Product.objects.get(name=product_name)
    image_list = ProductImage.objects.filter(product=product)
    detail_image_list = ProductDetailImage.objects.filter(product=product)
    update_context = {
        'product':product, 
        'brochure':Download.objects.filter(product=product, category='brochure').first(),
        'manual':Download.objects.filter(product=product, category='manual').first(),
        'sheet':Download.objects.filter(product=product, category='sheet').first(),
        'thumbnail':image_list[0],
        'image_list':image_list[1:], 
        'detail_image_list':detail_image_list,
    }
    context.update(update_context)
    print(context)
    return render(request, "detail.html", context=context)

def category_list(request, main_category, category_name):
    context = api_common.get_common_context()
    category = Category.objects.get(main_category=main_category, name=category_name)
    product_list = Product.objects.filter(category=category)
    for product in product_list:
        thumbnail = ProductImage.objects.filter(product=product).first()
        product.thumbnail = thumbnail.image
    context['product_list'] = product_list
    return render(request, "list.html", context=context)