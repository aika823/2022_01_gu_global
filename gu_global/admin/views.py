import json
from django.http import JsonResponse


from multiprocessing import context
from django.shortcuts import redirect, render
from products.models import BestProduct, Category, Product, ProductDetailImage, ProductImage

from support.models import Contact, Notice, NoticeImage, Popup, Video
from .models import Admin
from django.contrib.auth.hashers import make_password, check_password

from api.decorators import admin_required
import api.api_image


@admin_required
def index(request):
    context = {}
    return render(request, "index.html", context=context)


# 로그인 

def login(request):
    
    if request.method == "POST":
        try:
            admin = Admin.objects.get(username=request.POST.get('username'))
            if(check_password(request.POST.get('password'), admin.password)):
                request.session['admin_id'] = admin.id
                return redirect('/admin')
            else:
                context = {'error': "비밀번호를 다시 입력해주세요"}
                return render(request, "login.html", context=context)
                return redirect('/admin/login', context=context)
        except:
            context = {'error': "아이디를 다시 입력해주세요"}
            return render(request, "login.html", context=context)
            return redirect('/admin/login', context=context)
    return render(request, "login.html")


def best_product(request, id=None):
    product = BestProduct.objects.get(id=id) if id else None
    context = {'best_product_list':BestProduct.objects.all().order_by('order'), 'product':product}
    return render(request, "best_product.html", context=context)


# 문의사항 관리
def category(request):
    context = {'category_list':Category.objects.all()}
    return render(request, "category.html", context=context)
def category_create(request):
    return render(request, "category_detail.html")    
def category_view(request, id):
    context = {'category':Category.objects.get(id=id)}
    return render(request, "category_detail.html", context=context)


# 제품 관리
def products(request):
    context = {'product_list':Product.objects.all()}
    return render(request, "products.html", context=context)
def products_create(request):
    context = {'category_list': Category.objects.all()}
    return render(request, "products_form.html", context=context)
def products_view(request,id):
    
    product = Product.objects.get(id=id)
    
    context = {
        'product':product,
        'category_list': Category.objects.all(),
        'image_list':ProductImage.objects.filter(product=product),
        'detail_image_list':ProductDetailImage.objects.filter(product=product),
        
        'selected':{
            'codec' : 'selected' if product.type == 'codec' else None,
            'camera' : 'selected' if product.type == 'camera' else None,
            'speaker_phone' : 'selected' if product.type == 'speaker_phone' else None,
            'guide' : 'selected' if product.type == 'guide' else None,
            'software' : 'selected' if product.type == 'software' else None,
        }
    }
    return render(request, "products_form.html", context=context)


# 문의사항 관리
def contact(request):
    context = {'contact_list':Contact.objects.all()}
    return render(request, "contact.html", context=context)
def contact_create(request):
    return render(request, "contact_detail.html")    
def contact_view(request, id):
    context = {'contact':Contact.objects.get(id=id)}
    return render(request, "contact_detail.html", context=context)


# 공지사항 관리
def notice(request):
    context = {'notice_list':Notice.objects.all()}
    return render(request, "notice.html", context=context)
def create_notice(request):
    return render(request, "notice_detail.html")    
def view_notice(request, id):
    context = {'notice':Notice.objects.get(id=id)}
    return render(request, "notice_detail.html", context=context)


# 동영상 관리
def video(request):
    context = {'video_list':Video.objects.all()}
    return render(request, "video.html", context=context)
def video_create(request):
    return render(request, "video_detail.html")    
def video_view(request, id):
    context = {'video':Video.objects.get(id=id)}
    return render(request, "video_detail.html", context=context)


# 팝업 관리
def popup(request):
    context = {'popup_list':Popup.objects.all()}
    return render(request, "popup.html", context=context)
def popup_create(request):
    return render(request, "popup_detail.html")    
def popup_view(request, id):
    context = {'popup':Popup.objects.get(id=id)}
    return render(request, "popup_detail.html", context=context)


# # 다운로드 관리
# def download(request):
#     context = {'download_list':Download.objects.all()}
#     return render(request, "download.html", context=context)
# def download_create(request):
#     # context = {'product_list':Product.objects.all()}
#     context = {}
#     return render(request, "download_detail.html", context=context)    
# def download_view(request, id):
#     download = Download.objects.get(id=id)
#     context = {
#         # 'product_list':Product.objects.all(),
#         'download':download,
#         'selected':{
#             'brochure': 'selected' if download.category=='brochure' else None,
#             'manual': 'selected' if download.category=='manual' else None,
#             'sheet': 'selected' if download.category=='sheet' else None,
#             'codec' : 'selected' if download.type == 'codec' else None,
#             'camera' : 'selected' if download.type == 'camera' else None,
#             'speaker_phone' : 'selected' if download.type == 'speaker_phone' else None,
#             'guide' : 'selected' if download.type == 'guide' else None,
#             'software' : 'selected' if download.type == 'software' else None,
#         }
#     }
#     return render(request, "download_detail.html", context=context)


# 관리자 기능 함수

def create(request):

    if request.method == "POST":

        table = request.POST.get('table')
        action = request.POST.get('action')
        id = request.POST.get('id')

        if table == 'notice':
            if id:
                item = Notice.objects.get(id=id)
            elif action == 'create':
                item = Notice()

        if table == 'category':
            if id:
                item = Category.objects.get(id=id)
            elif action == 'create':
                item = Category()
        
        if table == 'contact':
            if id:
                item = Contact.objects.get(id=id)
            elif action == 'create':
                item = Contact()

        if table == 'video':
            if id:
                item = Video.objects.get(id=id)
            elif action == 'create':
                item = Video()
            if request.FILES.get('image'):
                item.image = request.FILES.get('image')
        
        if table == 'popup':
            if id:
                item = Popup.objects.get(id=id)
            elif action == 'create':
                item = Popup()
            item.image = request.FILES.get('image')

        if table == 'best_product':
            if id:
                item = BestProduct.objects.get(id=id)
            else:
                item = BestProduct()
            if request.FILES.get('image'):
                item.image = request.FILES.get('image')

        # if table == 'download':
        #     if id:
        #         item = Download.objects.get(id=id)
        #     elif action == 'create':
        #         item = Download()
            
        #     if request.FILES.get('manual'):
        #         item.manual = request.FILES.get('manual')
        #     if request.FILES.get('brochure'):
        #         item.brochure = request.FILES.get('brochure')
        #     if request.FILES.get('sheet'):
        #         item.sheet = request.FILES.get('sheet')

        if table == 'product':
            if id:
                item = Product.objects.get(id=id)
            elif action == 'create':
                item = Product()

            try:
                category = Category.objects.get(name=request.POST.get('category'))
            except:
                category = Category(name=request.POST.get('category'))
                category.save()

            if request.FILES.get('manual'):
                item.manual = request.FILES.get('manual')
            if request.FILES.get('brochure'):
                item.brochure = request.FILES.get('brochure')
            if request.FILES.get('sheet'):
                item.sheet = request.FILES.get('sheet')
                
            setattr(item, 'category', category)

        for key in request.POST:
            try:
                if key not in ['image', 'file', 'manual', 'brochure', 'sheet']:
                    setattr(item, key, request.POST.get(key))
            except:
                pass
        item.save()

        return redirect("/admin/{}/{}".format(table, item.id))

def delete(request):
    table = request.POST.get('table')
    id = request.POST.get('id')

    if table == 'video':
        Video.objects.get(id=id).delete()
        return redirect("/admin/video")
    
    # if table == 'download':
    #     Download.objects.get(id=id).delete()
    #     return redirect("/admin/download")

    if table == 'category':
        Category.objects.get(id=id).delete()
        return redirect("/admin/category")

    if table == 'best_product':
        BestProduct.objects.get(id=id).delete()
        return redirect("/admin/best_product")

    if table == 'product':
        Product.objects.get(id=id).delete()
        return redirect("/admin/product")

    if table == 'product_image':
        product_id = ProductImage.objects.get(id=id).product.id
        ProductImage.objects.get(id=id).delete()
        return redirect("/admin/{}/{}".format('product', product_id))
    
    if table == 'product_detail_image':
        product_id = ProductDetailImage.objects.get(id=id).product.id
        ProductDetailImage.objects.get(id=id).delete()
        return redirect("/admin/{}/{}".format('product', product_id))
    
    if table == 'popup':
        Popup.objects.get(id=id).delete()
        return redirect("/admin/popup")

    if table == 'notice':
        Notice.objects.get(id=id).delete()
        return redirect("/admin/notice")

def update_image(request):
    api.api_image.update_image(request)
    table = request.POST.get('table')
    id = request.POST.get('id')
    return redirect("/admin/{}/{}".format(table, id))

def update_detail_image(request):
    api.api_image.update_detail_image(request)
    table = request.POST.get('table')
    id = request.POST.get('id')
    return redirect("/admin/{}/{}".format(table, id))

def upload_image(request):  
    print(request.FILES.get('image'))
    image = NoticeImage()
    image.image = request.FILES.get('image')
    image.save()

    
    return JsonResponse({'url':str(image.image)})
    
