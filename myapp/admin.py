from django.contrib import admin
from .models import contact
from import_export.admin import ImportExportModelAdmin


# Register your models here.

class showdata(ImportExportModelAdmin):
    list_display = ('name', 'email', 'phone','city','pincode','investment', 'date')
    list_filter = ['date']

admin.site.register(contact,showdata)