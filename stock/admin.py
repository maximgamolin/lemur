from django.contrib import admin

from stock import models


@admin.register(models.Dataset)
class DatasetAdmin(admin.ModelAdmin):

    class PricingDatasetInline(admin.StackedInline):
        model = models.PricingDataset

    class DatasetPermissionsInline(admin.StackedInline):
        model = models.DatasetPermissions

    prepopulated_fields = {'slug': ('name',)}
    inlines = [
        PricingDatasetInline,
        DatasetPermissionsInline
    ]


@admin.register(models.DatasetPermissions)
class DatasetPermissionsAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PricingDataset)
class PricingDataset(admin.ModelAdmin):
    pass
