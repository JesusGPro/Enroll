from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display  = ('id', 'name', 'email', 'password')

""" 
The same could has been done:
class UserAdmin(admin.ModelAdmin):
    list_display  = ('id', 'name', 'email', 'password')
    
admin.site.register(User, UserAdmin)

"""