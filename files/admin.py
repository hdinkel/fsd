from django.contrib import admin
from django.contrib import messages

# Register your models here.

from .models import File, FileType, Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner',)
    search_fields = ['name']

class FileAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'hash', 'uuid', 'filesize', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    list_display = ('name', 'hash', 'uuid', 'filesize', 'created_at', 'updated_at')
    list_filter = ('project','project__owner')
    list_per_page = 100
    ordering = ('-created_at',)
    radio_fields = {'filetype': admin.HORIZONTAL, }  # Show as radio_buttons
    search_fields = ('name', 'hash')
    autocomplete_fields = ['project', 'filetype']


#    def __meta__(self):
#        self.verbose_name_plural = 'Files'

class FileTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'filetype', 'ext',)
    search_fields = ['name']

admin.site.register(File, FileAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(FileType, FileTypeAdmin)
