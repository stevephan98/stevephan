# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from django.shortcuts import render
from .models import Job

from django.shortcuts import render

def home(request):
    jobs = Job.objects 
    return render(request, 'jobs/home.html', {'jobs':jobs})