from django.contrib import admin

from .models import Equipment, Recording, Beat


class RecordingAdmin(admin.ModelAdmin):
  list_display = (
    "timeslot",

  )


admin.site.register(Recording, RecordingAdmin)
admin.site.register(Equipment)
admin.site.register(Beat)