from content.models import MenuHeaderItem, MenuMainItem, PhoneNumber, SocialNetwork


def menu_processor(requset):
	menu_header = MenuHeaderItem.objects.order_by('order')
	menu_main_nodes = MenuMainItem.objects.root_nodes()
	menu_phones = PhoneNumber.objects.all()
	social_nets = SocialNetwork.objects.all()
	return {'menu_header':menu_header,
			'menu_main_nodes':menu_main_nodes,
			'menu_phones':menu_phones,
			'social_nets':social_nets}