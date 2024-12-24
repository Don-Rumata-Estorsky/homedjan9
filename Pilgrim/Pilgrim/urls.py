


from django.contrib import admin
from django.urls import path, re_path
from app.views import *
from app import views


from django.shortcuts import redirect


urlpatterns = [
    path('admin/', admin.site.urls),
    
 path('json/', viewer, name='json'),
    path('redirect/', redirect, name='redirect'),
  path('only-get/', only_get, name='only_get'),
]



