from django.contrib import admin
# TODO
from petsta.common.models import PhotoComment


@admin.register(PhotoComment)
class CommonAdmin(admin.ModelAdmin):
    pass
