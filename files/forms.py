from django import forms
from .models import Project

class ZipfileUploadForm(forms.Form):
    file_field = forms.FileField()
    project = forms.ModelChoiceField(queryset=Project.objects.all(), empty_label="(No project)")

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ZipfileUploadForm, self).__init__(*args, **kwargs)
        print(self.user)
        self.fields['project'].queryset = Project.objects.filter(owner=self.user)


# class MultifileUploadForm(forms.Form):
#     file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
#     description = forms.CharField(widget=forms.Textarea)
#
#     def process_multiple_files(self):
#         print('Processing multiple files')
#         # TODO implement
