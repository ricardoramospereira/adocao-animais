from django.contrib import admin
from .models import PedidoAdocao

# Register your models here.
@admin.register(PedidoAdocao)
class PedidoAdocaoAdmin(admin.ModelAdmin):
    list_display = ("pet", "status")