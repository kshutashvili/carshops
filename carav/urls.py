"""carav URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView

from content.views import index, blog, article, catalog, login, ajax, basket,\
                          personal

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index.index, name='home'),
    url(r'^blog/$', blog.BlogList.as_view(), name='blog'),
    url(r'^category/$', TemplateView.as_view(template_name="category.html")),
    url(r'^blog/article/(?P<pk>\d+)/$', article.ArticleDetail.as_view(), name="article"),
    url(r'^contacts/$', TemplateView.as_view(template_name='contacts.html'), name='contacts'),
    url(r'^catalog/$', catalog.ProductList, name='catalog'),
    url(r'^basket/$', basket.basket, name="basket"),
    url(r'^personal/$', personal.personal, name='personal'),
    url(r'^personal/password/$', personal.change_password, name='change_pass'),
    url(r'^personal/orders/$', personal.orders, name='lk_orders'),
    url(r'^personal/contact/$', personal.contact, name='lk_contact'),
    url(r'^personal/waiting/$', personal.waiting, name='lk_waiting'),
    url(r'^product/$', TemplateView.as_view(template_name='tovar.html'), name='product'),
    url(r'^login/$', login.user_login, name='login'),
    url(r'^logout/$', login.user_logout, name='logout'),
    url(r'^register/$', login.user_create, name='register'),
    url(r'^order/$', basket.basket, name="order"),
    url(r'^ajax/add_product/$', ajax.basket_session, name='basket_session'),
    url(r'^ajax/news_generate/$', ajax.news_generate, name='news_gen'),
    url(r'^ajax/products_discount_generate/$', ajax.products_discount_generate, name='prod_disc_gen'),
    url(r'^ajax/car_select/$', ajax.car_select, name='car_select'),
    url(r'^ajax/change_amount/$', ajax.change_amount, name='change_amount'),
    url(r'^ajax/clear_basket/$', ajax.clear_basket, name='clear_basket')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

