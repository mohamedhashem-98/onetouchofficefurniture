from django.contrib import admin
from django.urls import path , include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('' , views.index , name='index'),
path('products/' , views.products , name='product'),
path('products/details/<int:id>' , views.details , name='detail'),
path('order/' , views.order , name='order'),
path('ar/' , views.indexar , name='indexar'),
path('ar/product/' , views.productsar , name='productsar'),
path('ar/products/details/<int:id>' , views.detailsar , name='detailar'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
