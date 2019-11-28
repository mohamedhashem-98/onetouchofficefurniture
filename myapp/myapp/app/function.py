from . import models

def getindexProducts():
    a =models.category.objects.filter(status=True)
    ProductsRel = {}
    for i in a:
       lst = []
       x =  models.product.objects.filter(category_id=i.category_id , status=True).order_by('-order')[:6]
       for j in x:
           lst.append(j)
       ProductsRel[i] = lst
    return ProductsRel

def getindexProductsar():
    a = models.category.objects.filter(status=True)
    ProductsRel = {}
    for i in a:
       lst = []
       x =  models.product.objects.filter(category_id=i.category_id , status=True).order_by('-order')[:6]
       for j in x:
           lst.append(j)
       ProductsRel[i.category_name_ar] = lst
    return ProductsRel

def getallproducts():
    a = models.category.objects.filter(status=True)
    ProductsRel = {}
    for i in a:
        lst = []
        x = models.product.objects.filter(category_id=i.category_id , status=True).order_by('-order')
        for j in x:
            lst.append(j)
        ProductsRel[i] = lst
    return ProductsRel

def getallproductsar():
    a = models.category.objects.filter(status=True)
    ProductsRel = {}
    for i in a:
        lst = []
        x = models.product.objects.filter(category_id=i.category_id , status=True).order_by('-order')
        for j in x:
            lst.append(j)
        ProductsRel[i.category_name_ar] = lst
    return ProductsRel

