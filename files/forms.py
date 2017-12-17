from django import forms
from .utils import extract_zipfile


class ZipfileUploadForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def process_zipfile(self):
        # send email using the self.cleaned_data dictionary
        print('Processing ZIPfile')
        extract_zipfile('/Users/dinkel/down/libraries.zip')
