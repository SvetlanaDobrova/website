from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path("", views.user_login, name='user_login'),
    ]
              #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
