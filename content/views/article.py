# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import DetailView

from content.models import Blog


class ArticleDetail(DetailView):
	model = Blog
	context_object_name = "article"
	template_name = "article.html"

