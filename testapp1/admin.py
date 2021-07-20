from django.contrib import admin
from testapp1.models import *
# Register your models here.
class RegistrationAdmin(admin.ModelAdmin):
    list_display=['name','email','password']
admin.site.register(login,RegistrationAdmin)
class RegistrationAdmin2(admin.ModelAdmin):
    list_display=['title','name','complete','created']
admin.site.register(taskmodel,RegistrationAdmin2)
