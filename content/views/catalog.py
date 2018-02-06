from django.shortcuts import render
from django.views.generic import ListView

from content.models import DiscountProduct, ProductImage, Banner


def ProductList(request):
    products = DiscountProduct.objects.all()
    images = ProductImage.objects.all()
    banners = Banner.objects.all()
    result = {}
    for obj in products:
        result[obj.product.id]=images.filter(product_id=obj.product.id)
    return render(request,'catalog.html',{'products':products,
                                          'banners':banners,
                                          'images':result})

