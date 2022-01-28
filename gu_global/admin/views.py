from multiprocessing import context
from django.shortcuts import redirect, render

from support.models import Notice
from .models import Admin
from django.contrib.auth.hashers import make_password, check_password
from api.decorators import admin_required


@admin_required
def index(request):
    context = {}
    return render(request, "index.html", context=context)


def login(request):
    # admin = Admin()
    # admin.username = "1234"
    # admin.password = make_password("1234")
    # admin.save()

    print(Admin.objects.all())
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



def products(request):
    context = {}
    return render(request, "products.html")


def contact(request):
    context = {}
    return render(request, "contact.html")


def notice(request):
    context = {'notice_list':Notice.objects.all()}
    return render(request, "notice.html", context=context)

def create_notice(request):
    return render(request, "notice_detail.html", context=context)
    return render(request, "notice_detail.html")
def view_notice(request, id):
    context = {'notice':Notice.objects.get(id=id)}
    return render(request, "notice_detail.html", context=context)


def download(request):
    context = {}
    return render(request, "download.html")


def video(request):
    context = {}
    return render(request, "video.html")


def popup(request):
    context = {}
    return render(request, "popup.html")




# @admin_required
# def reservation(request, room_id):
#     room = Room.objects.get(id=room_id)
#     room_reservation_list = RoomReservation.objects.filter(room=room)
#     context = {
#         "room":room,
#         "room_reservation_list": room_reservation_list,
#         "type_list" : get_type_list(),
#         "room_list" : Room.objects.all()
#     }

#     if request.method == "POST":
#         confirm_reservation(request.POST.get('id'))
    
#     return render(request, "manage_reservation.html", context=context)


# @admin_required
# def peak_season(request):
#     if request.method == "POST":
    
#         start = request.POST.get("start")
#         end = request.POST.get("end")
#         action = request.POST.get("action")

#         start_date = str_to_date(start)
#         end_date = str_to_date(end)
#         delta = end_date - start_date  
#         date_list = list()
#         for i in range(delta.days+1): 
#             day = start_date + timedelta(days=i)
#             date_list.append(day)
        
#         if action == "set":
#             for date in date_list:
#                 try:
#                     peak_season = PeakSeoson.objects.get(date=date)
#                 except:
#                     peak_season = PeakSeoson()
#                     peak_season.date = date
#                     peak_season.save()

#         if action == "delete":
#             for date in date_list:
#                 try:
#                     peak_season = PeakSeoson.objects.get(date=date)
#                     peak_season.delete()
#                 except:
#                     pass
    
#     peak_season = PeakSeoson.objects.all()
#     context = {
#         "peak_season": peak_season,
#         "type_list" : get_type_list(),
#         "room_list" : Room.objects.all()
#     }
#     return render(request, "peak_season.html", context=context)




def create(request):

    if request.method == "POST":

        print(request.POST)
        for i in request.POST:
            print(request.POST.get(i))

        table = request.POST.get('table')
        action = request.POST.get('action')
        id = request.POST.get('id')

        if table == 'notice':
            if id:
                item = Notice.objects.get(id=id)
            elif action == 'update':
                item = Notice()
            item.order = request.POST.get('order')
            item.title = request.POST.get('title')
            item.content = request.POST.get('content')
            item.author = request.POST.get('author')
            item.views = request.POST.get('views')

        
        
        item.save()

        return redirect("/admin/{}/{}".format(table, item.id))



# def update_image(request):

#     if request.method == "POST":

#         room_id = request.POST.get('room_id')
#         room = Room.objects.get(id=room_id)

#         image_list = request.FILES.getlist('image_list')
#         room_image_id_list = request.POST.getlist('room_image_id[]') 
#         room_image_index_list = list()
#         for index in request.POST.getlist('room_image_index[]'):
#             if index:
#                 room_image_index_list.append(int(index))
        
#         update_image_list = request.FILES.getlist('image_update[]') 
        
#         if image_list:
#             for img in image_list:
#                 image = Image(image=img)
#                 image.save()
#                 room_image = RoomImage(room=room, image=image)
#                 room_image.save()
                
#         if room_image_id_list:
#             i=0
#             for idx in range(len(room_image_id_list)):
#                 if idx in room_image_index_list:
#                     room_image = RoomImage.objects.get(id=room_image_id_list[idx])
#                     room_image.image.image.delete()
#                     room_image.image.image = update_image_list[i]
#                     i+=1
#                     room_image.image.save()

#         return redirect("/admin/room/{}".format(room_id))


# @admin_required
# def create_type(request, table):
#     context = {
#         "category": table,
#         "function":"create",
#         "type_list" : get_type_list(),
#         "room_list" : Room.objects.all()
#     }
#     return render(request, "create.html", context=context)


# @admin_required
# def create_room(request, table, id):
#     type = Type.objects.get(id=id)
#     context = {
#         "category": 'room',
#         "function":"create",
#         "type_list" : get_type_list(),
#         "room_list" : Room.objects.all(),
#         "type" : type
#     }
#     return render(request, "create.html", context=context)


# @admin_required
# def detail(request, table, id):

#     if table == "type":
#         item = Type.objects.get(id=id)
#     elif table == "room":
#         item = Room.objects.get(id=id)
#         item.image_list = RoomImage.objects.filter(room=item)
#         item.checkin_time = item.checkin_time.strftime('%H:%M')
#         item.checkout_time = item.checkout_time.strftime('%H:%M')
    
#     context = {
#         "category":table,
#         "id":id,
#         "item":item,
#         "function":"update",
#         "type_list" : get_type_list(),
#         "room_list" : Room.objects.all()
#     }
        
#     return render(request, "create.html", context=context)


# def delete(request):
    
#     if request.method == "POST":
        
#         table = request.POST.get('table')
#         id = request.POST.get('id')
#         room_id = request.POST.get('room_id')
        
#         if table == "type":
#             item = Type.objects.get(id=id)
#             item.delete()

#             return redirect("/admin/")
        
#         if table == "room":
#             item = Room.objects.get(id=id)
#             item.delete()

#             return redirect("/admin/")

#         if table == "room_image":
            
#             room_image_id = request.POST.get('room_image_id')
            
#             item = RoomImage.objects.get(id=room_image_id)
#             room_id = item.room.id
#             image_item = item.image
#             image = image_item.image

#             image.delete()
#             image_item.delete()
#             item.delete()

#             return redirect("/admin/room/{}".format(room_id))


# @admin_required
# def notification(request):
#     if request.method == "POST":
#         id_list = request.POST.getlist('notification_id[]')
#         for i in range(0, len(id_list)):
#             notification = Notification.objects.get(id=id_list[i])
#             notification.name = request.POST.getlist('notification_name[]')[i]
#             notification.content = request.POST.getlist('notification_content[]')[i]
#             notification.save()

#     context = {
#         'notification_list':Notification.objects.all()
#     }
#     return render(request, 'notification.html', context=context)