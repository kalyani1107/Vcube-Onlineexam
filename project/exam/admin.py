from django.contrib import admin
from . models import Registrationform

# Register your models here.

class appadmin(admin.ModelAdmin):
    list_display=['firstname','lastname','email','course','gender']
    list_filter=['firstname']

admin.site.register(Registrationform,appadmin)

