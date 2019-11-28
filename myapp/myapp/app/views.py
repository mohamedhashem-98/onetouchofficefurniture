from django.shortcuts import render, redirect
from . import models
import datetime
from app import function
from django.core.mail import send_mail
from django.http import HttpResponse


# Create your views here.
def index(request):
    company = models.company.objects.all()
    about = models.about.objects.all()
    slider = models.slider.objects.all()
    category = models.category.objects.filter(status=True)
    product_new = models.product.objects.filter(new_arrival=True , status=True).order_by('-order')[:4]
    services = models.services.objects.all()
    sales_order = models.sales_order.objects.all()
    products = models.product.objects.filter(status=True)
    ProductsRel = function.getindexProducts()

    data = {
        'company_data': company,
        'about_data': about,
        'product_new': product_new,
        'slider_data': slider,
        'services_data': services,
        'ProductsRel': ProductsRel,
    }
    if len(product_new) >= 1:
        data['p1'] = product_new[0]
    if len(product_new) >= 2:
        data['p2'] = product_new[1]
    if len(product_new) >= 3:
        data['p3'] = product_new[2]
    if len(product_new) >= 4:
        data['p4'] = product_new[3]
    if request.method == 'POST' and request.POST.get('bts') :
        tmp = request.POST['txt']
        request.session['KEY'] = tmp
        if len(models.product.objects.filter(product_name_en__contains=tmp)) > 0:
            return redirect('product')
        else:
            del request.session['KEY']
    if request.method == 'POST' and request.POST.get('submit'):
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        tmp = models.sales_order(name=name , phone_num=phone , email=email , full_text=message , date=datetime.datetime.now())
        tmp.save()
        send_mail(
            'One Furniture',
            "Name : " + name + "\n" +
            "Email : " + email + "\n" + 
            "Phone : " + phone + "\n" + 
            "Message : " + message + "\n",
            email,
            ['info@onetouchofficefurniture.com', 'hashim@algawhar.com'],
            fail_silently=False,
        )
        send_mail(
            'One Furniture',
            "Dear: " + name + " , you Already Recieved Your Message : " + message + "\n Thanks For Choosing Us And We Will Contact With You By Phone Or E-Mail Soon \n Thanks For You Mr/Mrs: " + name,
            'info@onetouchofficefurniture.com',
            [email],
            fail_silently=False,
        )
        return redirect('order')


    return render(request , "static_pages/index.html" , data)
def order(request):
  return redirect('index')
def details(request , id):
    if models.product.objects.filter(product_id=id) :
        x = models.product.objects.filter(product_id=id)
        company = models.company.objects.all()
        slider = models.slider.objects.all()
        if request.method == 'POST':
            name = request.POST['name']
            phone = request.POST['phone']
            email = request.POST['email']
            message = request.POST['message']
            tmp = models.sales_order(name=name, phone_num=phone, email=email, full_text=message,
                                     date=datetime.datetime.now())
            tmp.save()
            send_mail(
            'One Furniture',
            "Name : " + name + "\n" +
            "Email : " + email + "\n" + 
            "Phone : " + phone + "\n" + 
            "Message : " + message + "\n",
            email,
            ['info@onetouchofficefurniture.com', 'hashim@algawhar.com'],
            fail_silently=False,
            )
            send_mail(
            'One Furniture',
            "Dear: " + name + " , you Already Recieved Your Message : " + message + "\n Thanks For Choosing Us And We Will Contact With You By Phone Or E-Mail Soon \n Thanks For You Mr/Mrs: " + name,
            'info@onetouchofficefurniture.com',
            [email],
            fail_silently=False,
            )
            return redirect('order')
        return render(request, "static_pages/details.html" , {'x': x , 'company_data': company, 'slider_data': slider})
    else:
        return redirect('index')


def products(request):
    boolstate = 1
    company = models.company.objects.all()
    about = models.about.objects.all()
    slider = models.slider.objects.all()
    category = models.category.objects.filter(status=True)
    products = models.product.objects.filter(status=True)
    ProductsRel = function.getallproducts()
    if request.session.get('KEY'):
        x = models.product.objects.filter(product_name_en__contains=request.session.get('KEY'))
        if len(x) > 0:
            boolstate = 0
            ProductsRel = x
        del request.session['KEY']
    print(boolstate)
    print(ProductsRel)
    data = {
        'company_data': company,
        'about_data': about,
        'slider_data': slider,
        'ProductsRel': ProductsRel,

    }
    if boolstate == 1:
        data['state'] = boolstate

    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        tmp = models.sales_order(name=name, phone_num=phone, email=email, full_text=message,
                                 date=datetime.datetime.now())
        tmp.save()
        send_mail(
            'One Furniture',
            "Name : " + name + "\n" +
            "Email : " + email + "\n" + 
            "Phone : " + phone + "\n" + 
            "Message : " + message + "\n",
            email,
            ['info@onetouchofficefurniture.com', 'hashim@algawhar.com'],
            fail_silently=False,
        )
        send_mail(
            'One Furniture',
            "Dear: " + name + " , you Already Recieved Your Message : " + message + "\n Thanks For Choosing Us And We Will Contact With You By Phone Or E-Mail Soon \n Thanks For You Mr/Mrs: " + name,
            'info@onetouchofficefurniture.com',
            [email],
            fail_silently=False,
        )
        return redirect('order')
    return render(request , "static_pages/products.html" , data)

def indexar(request):
    company = models.company.objects.all()
    about = models.about.objects.all()
    slider = models.slider.objects.all()
    category = models.category.objects.filter(status=True)
    product_new = models.product.objects.filter(new_arrival=True , status=True).order_by('-order')[:4]
    services = models.services.objects.all()
    sales_order = models.sales_order.objects.all()
    products = models.product.objects.filter(status=True)
    ProductsRel = function.getindexProductsar()

    data = {
        'company_data' : company ,
        'about_data' : about ,
        'product_new' : product_new ,
        'slider_data' : slider,
        'services_data':services,
        'ProductsRel' : ProductsRel,
    }
    if len(product_new) >= 1 :
        data['p1'] = product_new[0]
    if len(product_new) >= 2 :
        data['p2'] = product_new[1]
    if len(product_new) >= 3 :
        data['p3'] = product_new[2]
    if len(product_new) >= 4 :
        data['p4'] = product_new[3]
    if request.method == 'POST' and request.POST.get('bts') :
        tmp = request.POST['txt']
        request.session['KEY'] = tmp
        if len(models.product.objects.filter(product_name_en__contains=tmp)) > 0:
            return redirect('productsar')
        else:
            del request.session['KEY']
    if request.method == 'POST' and request.POST.get('submit'):
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        tmp = models.sales_order(name=name , phone_num=phone , email=email , full_text=message , date=datetime.datetime.now())
        tmp.save()
        send_mail(
            'One Furniture',
            "Name : " + name + "\n" +
            "Email : " + email + "\n" + 
            "Phone : " + phone + "\n" + 
            "Message : " + message + "\n",
            email,
            ['info@onetouchofficefurniture.com', 'hashim@algawhar.com'],
            fail_silently=False,
        )
        send_mail(
            'One Furniture',
            "Dear: " + name + " , you Already Recieved Your Message : " + message + "\n Thanks For Choosing Us And We Will Contact With You By Phone Or E-Mail Soon \n Thanks For You Mr/Mrs: " + name,
            'info@onetouchofficefurniture.com',
            [email],
            fail_silently=False,
        )
        return redirect('order')


    return render(request , "static_pages/indexar.html" , data)

def detailsar(request , id):
    if models.product.objects.filter(product_id=id) :
        x = models.product.objects.filter(product_id=id)
        company = models.company.objects.all()
        slider = models.slider.objects.all()
        if request.method == 'POST':
            name = request.POST['name']
            phone = request.POST['phone']
            email = request.POST['email']
            message = request.POST['message']
            tmp = models.sales_order(name=name, phone_num=phone, email=email, full_text=message,
                                     date=datetime.datetime.now())
            tmp.save()
            send_mail(
            'One Furniture',
            "Name : " + name + "\n" +
            "Email : " + email + "\n" + 
            "Phone : " + phone + "\n" + 
            "Message : " + message + "\n",
            email,
            ['info@onetouchofficefurniture.com', 'hashim@algawhar.com'],
            fail_silently=False,
            )
            send_mail(
            'One Furniture',
            "Dear: " + name + " , you Already Recieved Your Message : " + message + "\n Thanks For Choosing Us And We Will Contact With You By Phone Or E-Mail Soon \n Thanks For You Mr/Mrs: " + name,
            'info@onetouchofficefurniture.com',
            [email],
            fail_silently=False,
            )
            return redirect('order')
        return render(request, "static_pages/detailsar.html" , {'x': x , 'company_data': company, 'slider_data': slider})
    else:
        return redirect('indexar')

def productsar(request):
    boolstate = 1
    company = models.company.objects.all()
    about = models.about.objects.all()
    slider = models.slider.objects.all()
    category = models.category.objects.filter(status=True)
    products = models.product.objects.filter(status=True)
    ProductsRel = function.getallproductsar()
    if request.session.get('KEY'):
        x = models.product.objects.filter(product_name_en__contains=request.session.get('KEY'))
        if len(x) > 0:
            boolstate = 0
            ProductsRel = x
        del request.session['KEY']
    data = {
        'company_data': company,
        'about_data': about,
        'slider_data': slider,
        'ProductsRel': ProductsRel,

    }
    if boolstate == 1:
        data['state'] = boolstate

    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        tmp = models.sales_order(name=name, phone_num=phone, email=email, full_text=message,
                                 date=datetime.datetime.now())
        tmp.save()
        send_mail(
            'One Furniture',
            "Name : " + name + "\n" +
            "Email : " + email + "\n" + 
            "Phone : " + phone + "\n" + 
            "Message : " + message + "\n",
            email,
            ['info@onetouchofficefurniture.com', 'hashim@algawhar.com'],
            fail_silently=False,
            )
        send_mail(
            'One Furniture',
            "Dear: " + name + " , you Already Recieved Your Message : " + message + "\n Thanks For Choosing Us And We Will Contact With You By Phone Or E-Mail Soon \n Thanks For You Mr/Mrs: " + name,
            'info@onetouchofficefurniture.com',
            [email],
            fail_silently=False,
            )
        return redirect('order')
    return render(request , "static_pages/productsar.html" , data)