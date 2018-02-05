# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from content.models import MenuHeaderItem, MenuMainItem, Information, SocialNetwork


def menu_processor(requset):
	menu_header = MenuHeaderItem.objects.order_by('order')
	menu_main_nodes = MenuMainItem.objects.root_nodes()
	information = Information.objects.all()
	phones = information.filter(information_type_id=1)
	emails = information.filter(information_type_id=2)
	addresses = information.filter(information_type_id=3)
	schedules = information.filter(information_type_id=4)
	social_nets = SocialNetwork.objects.all()
	return {'menu_header': menu_header,
			'menu_main_nodes': menu_main_nodes,
			'phones': phones,
			'emails': emails,
			'addresses': addresses,
			'schedules': schedules,
			'social_nets':social_nets}