from django.contrib import admin

from core import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(models.UserPayment)
class UserPaymentAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', )
    list_display = ('user', 'amount', 'currency')
