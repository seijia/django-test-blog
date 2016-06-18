from django.contrib import admin
from .models import Blog,Tag,Comment
#from  .forms import BlogForm
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','create')
    #form = BlogForm


admin.site.register(Blog,BlogAdmin)
admin.site.register(Tag)
admin.site.register(Comment)

