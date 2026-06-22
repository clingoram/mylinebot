from django.contrib import admin
from .models import Person,Message

# Register your models here.
class user_admin(admin.ModelAdmin):
  list_display = ('id','account','updatedAt','createdAt')

class user_message(admin.ModelAdmin):
  list_display = ('id','contentKeyWord','createdAt')

admin.site.register(Person, user_admin)
admin.site.register(Message,user_message)