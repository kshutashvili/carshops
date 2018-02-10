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
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView

from content.views import index, blog, article, catalog, login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index.index, name='home'),
    url(r'^blog/$', blog.BlogList.as_view(), name='blog'),
    url(r'^category/$', TemplateView.as_view(template_name="category.html")),
    url(r'^blog/article/(?P<pk>\d+)/$', article.ArticleDetail.as_view(), name="article"),
    url(r'^catalog/$', catalog.ProductList, name='catalog'),
    url(r'^basket/$', TemplateView.as_view(template_name="basket.html"), name="basket"),
    url(r'^personal/$', login.personal, name='personal'),
    url(r'^login/$', login.user_login, name='login'),
    url(r'^register/$', login.user_create, name='register')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

