from django.http import HttpResponse
from django.shortcuts import redirect

def allowed_roles(roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.groups.exists():

                grupos_usuario = [g.name for g in request.user.groups.all()]


                if any(grupo in roles for grupo in grupos_usuario):
                    return view_func(request, *args, **kwargs)
                else:
                    return redirect('index')
            else:
                return redirect('login')
        return wrapper_func
    return decorator


def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.exists():
            grupos_usuario = [g.name for g in request.user.groups.all()]
            if 'administradores' in grupos_usuario or 'admin1' in grupos_usuario:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('index')
        else:
            return redirect('login')
    return wrapper_func
