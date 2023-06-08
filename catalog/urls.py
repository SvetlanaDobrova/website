from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("service/<int:service_id>/", views.detail, name="detail"),
    path("group/<int:group_id>/", views.groupDetail, name="groupDetail")
]