# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from content.models import MenuMainItem, MenuHeaderItem, PhoneNumber, DealerSection, SocialNetwork, LandingProductBlock, Blog


admin.site.register(MenuHeaderItem)
admin.site.register(MenuMainItem)
admin.site.register(PhoneNumber)
admin.site.register(DealerSection)
admin.site.register(SocialNetwork)
admin.site.register(LandingProductBlock)
admin.site.register(Blog)