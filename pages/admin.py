
from django.contrib import admin
from .models import Page

class PageAdmin(admin.ModelAdmin):
    readonlyfields = ('created', 'updated')

admin.site.register(Page, PageAdmin)
