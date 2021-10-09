from django.contrib import admin

from market import models


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CollectionItem)
class CollectionItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.UserPurchases)
class UserPurchasesAdmin(admin.ModelAdmin):
    pass
