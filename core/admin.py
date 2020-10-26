from django.contrib import admin
from .models import Equipamento, Garantia

class GarantiaInLine(admin.TabularInline):
    model = Garantia
    extra = 1

class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ['n_invent', 'tipo', 'filial', 'status']
    inlines = [
        GarantiaInLine
    ]

admin.site.register(Equipamento, EquipamentoAdmin)
admin.site.register(Garantia)
