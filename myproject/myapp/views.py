from django.shortcuts import render
from myapp.models import *
from django.core import serializers
import json
from django.http import JsonResponse
# Create your views here.


def gettask(request):
    ob = list(task.objects.values())
    return JsonResponse(ob, safe=False)
