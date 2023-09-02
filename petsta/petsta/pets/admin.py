from django.contrib import admin
# TODO
from petsta.pets.models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass

