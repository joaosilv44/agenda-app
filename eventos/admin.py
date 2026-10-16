from django.contrib import admin
from .models import (
    Evento,
    Local,
    Categoria,
    Atividade,
    Inscricao,
    Relatorio,
)

class AtividadeInline(admin.TabularInline):
    model = Atividade
    extra = 1

class RelatorioInline(admin.StackedInline):
    model = Relatorio
    extra = 0
    max_num = 1

@admin.register
class EventoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "inicio", "local")
    list_filter = ("local", "categoria")
    search_fields = ("titulo",)

    inlines = [
        AtividadeInline,
        RelatorioInline,
    ]

admin.site.register(Local)
admin.site.register(Categoria)
admin.site.register(Inscricao)
admin.site.register(Evento)
admin.site.register(Atividade)