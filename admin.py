from django.contrib import admin
from .models import Page
# Register your models here.
#in case of custom user not default syntax....
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display=['user_name','password']

# @admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['user', 'pag_name', 'pag_cat', 'pag_publish_date']

admin.site.register(Page, PageAdmin)