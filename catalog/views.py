from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import BeautyService
# Create your views here.

def index(request):
    ServiceList = BeautyService.objects.all()
    template = loader.get_template("index.html")
    context = {
        "ServiceList": ServiceList,
    }

    return HttpResponse(template.render(context, request))

def detail(request, service_id):
    service = BeautyService.objects.get(id=service_id)
    template = loader.get_template("service.html")
    context = {
        "service": service
    }
    return HttpResponse(template.render(context, request))