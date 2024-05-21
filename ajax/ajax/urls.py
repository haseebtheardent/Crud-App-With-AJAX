from django.contrib import admin
from django.urls import path
from app.views import my_form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', my_form, name='my_form'),    
]
