from django.contrib import admin
from .models import User,Message

# Register your models here.
class user_admin(admin.ModelAdmin):
    list_display = ('uid','account','updated_at','created_at')

class message(admin.ModelAdmin):
    list_display = ('user_id','contentKeyWord')

admin.site.register(User, user_admin)
admin.site.register(Message,message)