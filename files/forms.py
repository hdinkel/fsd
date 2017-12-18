from django import forms

class ZipfileUploadForm(forms.Form):
    file_field = forms.FileField()
    description = forms.CharField(widget=forms.Textarea)


class MultifileUploadForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    description = forms.CharField(widget=forms.Textarea)

    def process_multiple_files(self):
        print('Processing multiple files')
        # TODO implement
