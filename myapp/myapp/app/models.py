from django.db import models

# Create your models here.
class company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name_en = models.CharField(max_length=255 , null=False)
    company_name_ar = models.CharField(max_length=255 , null=False)
    address_en = models.CharField(max_length=255 , null=True )
    address_ar = models.CharField(max_length=255 , null=True)
    phone = models.CharField(max_length=100 , null=True, blank=True)
    whatsapp = models.CharField(max_length=255 , null=True, blank=True)
    Facebook = models.CharField(max_length=255 , null=True, blank=True)
    google_business = models.CharField(max_length=255 , null=True, blank=True)
    youtube = models.CharField(max_length=255 , null=True, blank=True)
    location = models.CharField(max_length=255 , null=True, blank=True)
    logo = models.ImageField(upload_to='photo/' , null=True , blank=True)
    short_description = models.TextField(null=True, blank=True)
    keywords_en = models.TextField(null=True, blank=True)
    keywords_ar = models.TextField(null=True, blank=True)

class about(models.Model):
    about_id = models.AutoField(primary_key=True)
    about_name_en = models.CharField(max_length=255 , null=True, blank=True)
    about_name_ar = models.CharField(max_length=255, null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    description_ar = models.TextField(null=True, blank=True)
    Image = models.ImageField(upload_to='photo/' , null=True , blank=True)
    Icon = models.ImageField(upload_to='photo/' , blank=True , null=True)

class slider(models.Model):
    slider_id = models.AutoField(primary_key=True)
    slider_name_en = models.CharField(max_length=255 , null=True, blank=True)
    slider_name_ar = models.CharField(max_length=255, null=True, blank=True)
    slider_description_en = models.TextField(null=True, blank=True)
    slider_description_ar = models.TextField(null=True, blank=True)
    order = models.IntegerField(null=False)
    Image = models.ImageField(upload_to='photo/', null=True, blank=True)
    logo = models.ImageField(upload_to='photo/', null=True, blank=True)

class category(models.Model):
    category_id = models.IntegerField(primary_key=True )
    category_name_en = models.CharField(max_length=255 , null=True, blank=True)
    category_name_ar = models.CharField(max_length=255, null=True, blank=True)
    status = models.BooleanField(null=False)
    order = models.IntegerField(null=False)
    Icon = models.ImageField(upload_to='photo/' , null=True, blank=True)
    Image = models.ImageField(upload_to='photo/' , null=True, blank=True)
    main_category_id = models.IntegerField(null=True)
    def __str__(self):
        return self.category_name_en



class product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name_en = models.CharField(max_length=255 , null=True, blank=True)
    product_name_ar = models.CharField(max_length=255, null=True, blank=True)
    category_id = models.ForeignKey(category , on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='photo/', null=True, blank=True)
    product_description_en = models.CharField(max_length=255 , null=True, blank=True)
    short_desc_en = models.CharField(max_length=255 , null=True, blank=True)
    short_desc_ar = models.CharField(max_length=255, null=True, blank=True)
    product_description_ar = models.CharField(max_length=255, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    old_price = models.IntegerField(null=True, blank=True)
    status = models.BooleanField(null=False)
    order = models.IntegerField(null=False)
    new_arrival = models.BooleanField(null=False)

class services(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name_en = models.CharField(max_length=255 , null=True, blank=True)
    service_name_ar = models.CharField(max_length=255, null=True, blank=True)
    service_icon = models.ImageField(upload_to='photo/' , null=True, blank=True)
    Image = models.ImageField(upload_to='photo/' , null=True, blank=True)
    status = models.BooleanField(null=False)
    service_desc_en = models.CharField(max_length=255, null=True, blank=True)
    service_desc_ar = models.CharField(max_length=255, null=True, blank=True)
    order = models.IntegerField(null=False)

class sales_order(models.Model):
    sales_order_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255 , null=False, blank=True)
    email = models.EmailField(null=False, blank=True)
    phone_num = models.CharField(max_length=255 , null=False, blank=True)
    date = models.DateTimeField(null=False, blank=True)
    full_text = models.TextField(null=True, blank=True)













