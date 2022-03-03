from django.contrib import admin
from cowapp.models import *
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['id','name','contact','email','address','comment','amount']
admin.site.register(User,UserAdmin)

class Amount_infoAdmin(admin.ModelAdmin):
    list_display = ['id','amount','user']

admin.site.register(Amount_info,Amount_infoAdmin)