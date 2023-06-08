from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import BeautyService, BeautyServiceGroup
# Create your views here.

def index(request): # страница с группами услуг
    GroupList = BeautyService.objects.raw("SELECT g.id, g.Name as Name, min(s.Price) as Price from catalog_beautyservicegroup g inner join catalog_beautyservice s on g.id = s.Group_id group by g.id, g.Name")
    template = loader.get_template("price.html")
    context = {
        "ServiceList": GroupList,
    }

    return HttpResponse(template.render(context, request))

def detail(request, service_id):
    service = BeautyService.objects.get(id=service_id)
    template = loader.get_template("service.html")
    context = {
        "service": service
    }
    return HttpResponse(template.render(context, request))

def groupDetail(request, group_id):
    serviceGroup = BeautyServiceGroup.objects.get(id=group_id)
    ServiceList = BeautyService.objects.all().filter(Group_id=group_id)
    #ServiceList = BeautyService.objects.raw("SELECT s.id, s.Name as Name, s.Price, s.Description from catalog_beautyservice s where s.Group_id = %s", [group_id])
    template = loader.get_template("serviceGroup.html")
    return HttpResponse(template.render({"Services":ServiceList, "serviceGroup":serviceGroup}, request))