from django.contrib import admin
from . import models

class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'city']

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'created', 'status']
    list_filter = ('category',)
    search_fields = ('title', 'body')
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(models.User, UserAdmin)
admin.site.register(models.Post, PostAdmin)