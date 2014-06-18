from django.contrib import admin

from .models import Bank

class BankAdmin(admin.ModelAdmin):
    class Meta:
        model = Bank
    list_display = ('name',)

admin.site.register(Bank, BankAdmin)