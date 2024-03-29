from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile
# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'url')

#dmin.site.register(Category)
admin.site.register(Page, PageAdmin)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
admin.site.register(Category, CategoryAdmin)
admin.site.register(UserProfile)