from django.contrib import admin

from apps.vps.models import VPSModel


@admin.register(VPSModel)
class VPSModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'cpu', 'ram', 'hdd', 'status', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('id',)
