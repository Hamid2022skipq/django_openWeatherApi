from django.contrib import admin
from abstracts.models import * 

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','age','fee']
@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display=['id','name','date','age','payment']
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=['id','name','date','age','salary']
