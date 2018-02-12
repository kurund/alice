from django.contrib import admin

# Register your models here.
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    pass

admin.site.register(Client, ClientAdmin)