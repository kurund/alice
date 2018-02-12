from django.contrib import admin

# Register your models here.
from .models import Partner

admin.site.site_header = 'ALICE: administration'
admin.site.site_title = 'ALICE: administration'

class PartnerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Partner, PartnerAdmin)