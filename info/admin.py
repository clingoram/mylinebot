from django.contrib import admin
from .models import Person,Message

# Register your models here.
class user_admin(admin.ModelAdmin):
  list_display = ('id','uid','account','updated_at','created_at')

class user_message(admin.ModelAdmin):
  list_display = ('uid','contentKeyWord')

admin.site.register(Person, user_admin)
admin.site.register(Message,user_message)