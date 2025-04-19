from django.http import HttpResponse
from django.shortcuts import redirect

def allowed_roles(roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.groups.exists():
                grupo = request.user.groups.all()[0].name
                if grupo in roles:
                    return view_func(request, *args, **kwargs)
                else:
                    return redirect('index')
            else:
                return redirect('login')
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        grupo = None
        if request.user.groups.exists():
            grupo = request.user.groups.all()[0].name

        if grupo == 'usuario':
            return redirect('index')
        if grupo == 'admin1':
            return view_func(request, *args, **kwargs)
    return wrapper_function
