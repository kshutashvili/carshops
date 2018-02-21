# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _

from content.models import Product, ProductImage, ChipBasket, Rait, ModelCar,\
                           TogetherCheaper, Comment


def tovar(request, pk):
    if request.method == 'GET':
        product = Product.objects.get(id=pk)
        raits = Rait.objects.all()
        images = ProductImage.objects.all()
        prod_images = ProductImage.objects.filter(product_id=pk)
        related_products = Product.objects.all()
        related_products_images = {}
        for obj in related_products:
            related_products_images[obj.id]=images.filter(product_id=obj.id)
        compatibility_models = product.get_compatibility_models()
        compatibilities = []
        temp = []
        for obj in compatibility_models:
            temp.append(obj.stamp.name)
            if temp not in compatibilities:
                compatibilities.append([obj.stamp.name])
                temp.pop()
            else:
                temp.pop()
        for i in range(0, len(compatibilities)):
            for j in range(0, len(compatibility_models)):
                if compatibilities[i][0] == compatibility_models[j].stamp.name:
                    compatibilities[i].append(compatibility_models[j])
        promotions_queryset = TogetherCheaper.objects.all()
        promotions = []
        for obj in promotions_queryset:
            if product in obj.products.iterator():
                promotions.append(obj)
        comments = Comment.objects.filter(product_id=pk) 
        return render(request,'tovar.html',{'related_products':related_products,
                                            'images':related_products_images,
                                            'product':product,
                                            'prod_images':prod_images,
                                            'raits':raits,
                                            'compatibilities':compatibilities,
                                            'promotions':promotions,
                                            'comments':comments})
    else:
        errors = []
        if not request.POST.get('name',''):
            errors.append('Ошибка')
        if not request.POST.get('msg',''):
            errors.append('Ошибка')
        if not errors:
            comment = Comment()
            comment.product = Product.objects.get(id=pk)
            comment.name = request.POST['name']
            comment.content = request.POST['msg']
            comment.save()
            return HttpResponseRedirect('%s?status_message=%s' % (reverse('product', kwargs={'pk':pk}),_('Отзыв успешно опубликован')))
        else:
            return HttpResponseRedirect('%s?status_message=%s' % (reverse('product', kwargs={'pk':pk}),_('Если хотите оставить отзыв, заполните все поля')))
        

