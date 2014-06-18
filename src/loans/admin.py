from django.contrib import admin

from .models import Credit

class CreditAdmin(admin.ModelAdmin):
    class Meta:
        model = Credit
    list_display = ('name', )

admin.site.register(Credit, CreditAdmin)
