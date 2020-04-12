from django.contrib import admin

from set.models import Set


class SetAdmin(admin.ModelAdmin):
    list_display = ["set_name", "set_value", "id"]


admin.site.register(Set)
