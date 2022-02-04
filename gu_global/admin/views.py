from multiprocessing import context
from django.shortcuts import redirect, render
from products.models import Category, Product, ProductDetailImage, ProductImage

from support.models import Notice
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
    
    # admin = Admin()
    # admin.username = "1234"
    # admin.password = make_password("1234")
    # admin.save()

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


# 제품 관리

def products(request):
    context = {
        'product_list':Product.objects.all()
    }
    return render(request, "products.html", context=context)

def products_create(request):
    context = {
        'category_list': Category.objects.all()
    }
    return render(request, "products_form.html", context=context)

def products_view(request,id):
    context = {
        'product':Product.objects.get(id=id),
        'category_list': Category.objects.all(),
        'image_list':ProductImage.objects.filter(product=Product.objects.get(id=id)),
        'detail_image_list':ProductDetailImage.objects.filter(product=Product.objects.get(id=id))
    }
    return render(request, "products_form.html", context=context)


# 문의사항 관리

def contact(request):
    context = {}
    return render(request, "contact.html")


# 공지사항 관리

def notice(request):
    context = {'notice_list':Notice.objects.all()}
    return render(request, "notice.html", context=context)

def create_notice(request):
    return render(request, "notice_detail.html")    

def view_notice(request, id):
    context = {'notice':Notice.objects.get(id=id)}
    return render(request, "notice_detail.html", context=context)


# 자료실 파일 관리

def download(request):
    context = {}
    return render(request, "download.html")


# 동영상 관리

def video(request):
    context = {}
    return render(request, "video.html")


# 팝업 관리

def popup(request):
    context = {}
    return render(request, "popup.html")


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
            setattr(item, 'category', category)

        for key in request.POST:
            try:
                setattr(item, key, request.POST.get(key))
            except:
                pass
        item.save()

        return redirect("/admin/{}/{}".format(table, item.id))

def delete(request):
    table = request.POST.get('table')
    id = request.POST.get('id')

    if table == 'product':
        Product.objects.get(id=id).delete()
        return redirect("/admin/product")

    if table == 'product_image':
        product_id = ProductImage.objects.get(id=id).product.id
        ProductImage.objects.get(id=id).delete()
        return redirect("/admin/{}/{}".format('product', product_id))
    
    if table == 'product_detail_image':
        print(id)
        product_id = ProductDetailImage.objects.get(id=id).product.id
        ProductDetailImage.objects.get(id=id).delete()
        return redirect("/admin/{}/{}".format('product', product_id))

def update_image(request):
    api.api_image.update_image(request)
    table = request.POST.get('table')
    id = request.POST.get('id')
    return redirect("/admin/{}/{}".format(table, id))

def update_detail_image(request):
    print(request.POST)
    api.api_image.update_detail_image(request)
    table = request.POST.get('table')
    id = request.POST.get('id')
    return redirect("/admin/{}/{}".format(table, id))