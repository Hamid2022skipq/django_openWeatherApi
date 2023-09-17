from django.contrib import admin
from .models import Post,Book

# Register your models here.
# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('user','title','publish_date')
admin.site.register(Post,PostAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display=('Users','title','pages','publish_date')
admin.site.register(Book,BookAdmin)