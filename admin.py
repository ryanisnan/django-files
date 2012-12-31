from django.contrib import admin

from files.models import File

class FileAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_uploaded',)
    search_fields = ('name',)

admin.site.register(File, FileAdmin)