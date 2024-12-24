from django.shortcuts import *
from django.http import *
from django.urls import *
from django.shortcuts import *
from .models import *
from django.urls import *



from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods


def viewer(request):
    data = {
        "message": "Это JSON-ответ",
        "status": "success"
    }
    return JsonResponse(data)


def redirect_view(request):
    
    url = reverse('json_response')
    return redirect(url)

@require_http_methods(["GET"])
def only_get(request):
    return JsonResponse({"message": "Только GET-запросы разрешены"})

from django.urls import path


urlpatterns = [
    path('json/', viewer, name='viewer'),
    path('redirect/', redirect, name='redirect'),
    path('only-get/', only_get, name='only_get'),
]

