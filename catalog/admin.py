from django.contrib import admin
from .models import BeautyService, BeautyServiceGroup, Feedback, Contacts

# Register your models here.

admin.site.register(BeautyService)
admin.site.register(BeautyServiceGroup)
admin.site.register(Feedback)
admin.site.register(Contacts)