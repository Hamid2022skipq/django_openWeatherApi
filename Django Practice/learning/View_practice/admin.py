from django.contrib import admin

# Register your models here.
from View_practice.models import service
class serviceAdmin(admin.ModelAdmin):
    list_display=('name','email','age','fee')
admin.site.register(service,serviceAdmin)
# ,'title''des',