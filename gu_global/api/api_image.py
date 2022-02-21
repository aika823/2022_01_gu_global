from products.models import Product, ProductDetailImage, ProductImage

def update_image(request):

    # 이미지 추가
    id = request.POST.get('id')
    product = Product.objects.get(id=id)
    image_list = request.FILES.getlist('image_list')
    if image_list:
        for img in image_list:
            product_image = ProductImage(product=product, image=img)
            product_image.save()

    # 이미지 수정
    update_image_id_list = [id for id in request.POST.getlist('update_image_id[]') if id] 
    update_image_list = request.FILES.getlist('update_image[]')
    for idx, val in enumerate(update_image_id_list):
        image = ProductImage.objects.get(id=val)
        image.image = update_image_list[idx]
        image.save()


def update_detail_image(request):

    # 이미지 추가
    id = request.POST.get('id')
    product = Product.objects.get(id=id)
    image_list = request.FILES.getlist('image_list')
    if image_list:
        for img in image_list:
            product_image = ProductDetailImage(product=product, image=img)
            product_image.save()

    # 이미지 수정
    update_image_id_list = [id for id in request.POST.getlist('update_image_id[]') if id] 
    update_image_list = request.FILES.getlist('update_image[]')
    for idx, val in enumerate(update_image_id_list):
        image = ProductDetailImage.objects.get(id=val)
        image.image = update_image_list[idx]
        image.save()


def delete_image(request):
    print(request)