from django.contrib import admin
from app.models import *

class companyAdmin(admin.ModelAdmin):
    list_display = ['company_name_en' , 'company_name_ar'  , 'address_en' , 'address_ar']
admin.site.register(company , companyAdmin)

class aboutAdmin(admin.ModelAdmin):
    list_display = ['about_name_en' , 'about_name_ar']
admin.site.register(about , aboutAdmin)

class sliderAdmin(admin.ModelAdmin):
    list_display = ['slider_name_en' , 'slider_name_ar' , 'order']
admin.site.register(slider , sliderAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display = ['category_name_en' , 'category_name_ar' , 'order' ,'status']
admin.site.register(category , categoryAdmin)

class productAdmin(admin.ModelAdmin):
    list_display = ['product_name_en' , 'product_name_ar' , 'category_id' ,'status' , 'price' , 'old_price' , 'status']
admin.site.register(product , productAdmin)

class servicesAdmin(admin.ModelAdmin):
    list_display = ['service_name_en' , 'service_name_ar' , 'order' ,'status']
admin.site.register(services , servicesAdmin)

class SalesOrderAdmin(admin.ModelAdmin):
    list_display = ['name' , 'email' , 'phone_num' ,'date']
admin.site.register(sales_order , SalesOrderAdmin)









