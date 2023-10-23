from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import sys
import os
import json
from django.shortcuts import render
from .models import *


def Index(request, *args, **kwargs):
    return render(request, 'index.html')


def post_create(request, *args, **kwargs):
    return render(request, 'new.html')
