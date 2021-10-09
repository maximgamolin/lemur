from django.contrib import admin

from plant import models


@admin.register(models.Workpiece)
class WorkpieceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.WorkpiecePricing)
class WorkpiecePricingAdmin(admin.ModelAdmin):
    pass


@admin.register(models.DataSampling)
class DataSamplingAdmin(admin.ModelAdmin):
    pass

