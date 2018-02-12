from django.shortcuts import render

from content.models import LandingProductBlock, Blog, Product, PopularProduct,\
                           DiscountProduct, ProductImage, ChipBasket


def index(request):
    landing_products = LandingProductBlock.objects.order_by('order').reverse()[:5]
    news = Blog.objects.order_by('date').filter(active=True).reverse()[:3]
    images = ProductImage.objects.all()
    discount_products = DiscountProduct.objects.all()
    discount_products_images = {}
    for obj in discount_products:
        discount_products_images[obj.product.id]=images.filter(product_id=obj.product.id)
    popular_products = PopularProduct.objects.all()
    popular_products_images = {}
    for obj in popular_products:
        popular_products_images[obj.product.id]=images.filter(product_id=obj.product.id)
    if not request.session.has_key('basket_id'):
        basket = ChipBasket()
        basket.save()
        request.session['basket_id'] = basket.id
    return render(request,'index.html',{'landing_products':landing_products,
                                        'products_disc':discount_products,
                                        'products_pop':popular_products,
                                        'disc_images':discount_products_images,
                                        'pop_images':popular_products_images,
                                        'news':news})

