from functools import wraps
from django.http import HttpResponseRedirect
from admin.models import Admin

def admin_required(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        admin_id = request.session.get('admin_id')
        try:
            admin = Admin.objects.get(id=admin_id)
        except:
            admin = None
        
        if admin:
            return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/admin/login')
    return wrap