from django import template


register = template.Library()


@register.inclusion_tag('news_gen.html')
def news_generate(news):
    return {'news':news}


@register.inclusion_tag('prod_disc_gen_block.html')
def products_discount_generate_block(products, images):
    return {'products':products,
            'images':images}


@register.inclusion_tag('prod_disc_gen_view.html')
def products_discount_generate_view(products, images):
    return {'products':products,
            'images':images}


@register.inclusion_tag('model_cars_generate.html')
def model_cars_generate(model_cars):
    return {'model_cars':model_cars}


@register.inclusion_tag('year_cars_generate.html')
def year_cars_generate(year_cars):
    return {'year_cars':year_cars}

