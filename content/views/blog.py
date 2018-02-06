# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView

from content.models import Blog


class BlogList(ListView):
	model = Blog
	context_object_name = "news"
	template_name = "blog.html"

	def get_queryset(self):
		news = Blog.objects.order_by('date').filter(active=True).reverse()[:3]
		return news