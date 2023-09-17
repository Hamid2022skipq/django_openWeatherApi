from django.contrib import admin
# Register your models here.
from TableRelationship.models import Page
@admin.register(Page)
class serviceAdmin(admin.ModelAdmin):
    list_display=('user','name','cattogare','publish_date')
# admin.site.register(Page,serviceAdmin)