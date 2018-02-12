from django.shortcuts import render,HttpResponse
from django.http import Http404

import datetime

# Create your views here.

def index(request):
    return render(request,"qcloudManage/index.html")
