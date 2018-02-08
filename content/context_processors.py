# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from content.models import MenuHeaderItem, MenuMainItem, Information, SocialNetwork, StampCar, ModelCar, YearCar


def menu_processor(requset):
	menu_header = MenuHeaderItem.objects.order_by('order')
	menu_main_nodes = MenuMainItem.objects.root_nodes()
	information = Information.objects.all()
	stamp_cars = StampCar.objects.all()
	model_cars = ModelCar.objects.all()
	year_cars = YearCar.objects.all()
	phones = information.filter(information_type_id=1)
	emails = information.filter(information_type_id=2)
	addresses = information.filter(information_type_id=3)
	schedules = information.filter(information_type_id=4)
	social_nets = SocialNetwork.objects.all()
	return {'menu_header': menu_header,
			'menu_main_nodes': menu_main_nodes,
			'stamp_cars':stamp_cars,
			'model_cars':model_cars,
			'year_cars':year_cars,
			'phones': phones,
			'emails': emails,
			'addresses': addresses,
			'schedules': schedules,
			'social_nets':social_nets}