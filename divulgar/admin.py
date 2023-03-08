from django.contrib import admin
from .models import Raca, Tag, Pet

# Register your models here.
@admin.register(Raca)
class RacaAdmin(admin.ModelAdmin):
    list_display = ("raca",)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("tag",)

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ("usuario", "nome", "raca", "status")