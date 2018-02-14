from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.http import Http404
import datetime

from qcloudManage.config import config as cfg
from QcloudApi.qcloudapi import QcloudApi


# Create your views here.

def index(request):
    qcloud = OperationQcloud()
    qcloud.active_region()
    return render(request,"qcloudManage/index.html")

#云平台操作类
class OperationQcloud():
    secretId = cfg["default"].SecretId
    secretKey = cfg["default"].SecretKey

    def active_region(self):
        module = 'cvm'
        action = 'DescribeRegions'
        config = {
	    'secretId': self.secretId,
	    'secretKey': self.secretKey
	}
        action_params = {
	}	
        try:
            service = QcloudApi(module, config)
            print(service.generateUrl(action, action_params))
            print(service.call(action, action_params))
        except Exception as e:
            import traceback
            print('traceback.format_exc():\n%s' % traceback.format_exc())
