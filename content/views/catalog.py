from django.shortcuts import render
from django.views.generic import ListView

from content.models import Product, ProductImage, Banner


def ProductList(request):
    products = Product.objects.all()[:2]
    images = ProductImage.objects.all()
    banners = Banner.objects.all()
    result = {}
    for obj in products:
        result[obj.id]=images.filter(product_id=obj.id)
    return render(request,'catalog.html',{'products':products,
                                          'banners':banners,
                                          'images':result})

