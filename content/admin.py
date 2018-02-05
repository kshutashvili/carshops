# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from content.models import MenuMainItem, MenuHeaderItem, DealerSection, SocialNetwork, LandingProductBlock, Blog, Information
from content.models import Product, DiscountProduct, PopularProduct


admin.site.register(MenuHeaderItem)
admin.site.register(MenuMainItem)
admin.site.register(DealerSection)
admin.site.register(SocialNetwork)
admin.site.register(LandingProductBlock)
admin.site.register(Blog)
admin.site.register(Information)
admin.site.register(Product)
admin.site.register(DiscountProduct)
admin.site.register(PopularProduct)