# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re

from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required

from content.models import Order


@login_required
def personal(request):
	if request.method == 'GET':
		orders = Order.objects.filter(user=request.user)
		return render(request, 'lk.personal.html', {'orders':orders})