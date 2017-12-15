from django.contrib import admin
from django.contrib import messages

# Register your models here.

from .models import File, FileType, Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner',)

class FileAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'hash', 'uuid', 'filesize', 'created_at', 'updated_at')
    list_display = ('name', 'hash', 'uuid', 'filesize', 'created_at', 'updated_at')

#    def __meta__(self):
#        self.verbose_name_plural = 'Files'

class FileTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'filetype', 'ext',)

admin.site.register(File, FileAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(FileType, FileTypeAdmin)
