from django.contrib import admin
from django.contrib import messages

# Register your models here.

from .models import File

class FileAdmin(admin.ModelAdmin):
    readonly_fields = ('hash', 'filesize', 'created_at', 'updated_at')

#    def save_model(self, request, obj, form, change):
#        if obj.id is None:
#            file = form.cleaned_data['file']
#            if not file:
#                messages.add_message(request, messages.ERROR, 'No File to save. Please check Input.')
#            else:
#                try:
#                    obj = File.objects.get(hash=hash)
#                    messages.add_message(request, messages.WARNING, 'Files with Hash "%s" already in DB' % hash)
#                except File.DoesNotExist:
#                    obj.hash = hash
#                    obj.save()


    def __meta__(self):
        self.verbose_name_plural = 'Files'

admin.site.register(File, FileAdmin)
