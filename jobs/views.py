# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def steve(request):
    return render(request, 'jobs/steve.html')