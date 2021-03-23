from django.contrib import admin

# Register your models here.
from .models import Institution, Investor, Signatory

admin.site.register(Institution)
admin.site.register(Investor)
# admin.site.register(Bank)
admin.site.register(Signatory)
# admin.site.register(Nextofkin)