from django.views.generic import DetailView, ListView, CreateView
from django.views.generic.edit import FormView
# from django.urls import reverse_lazy, reverse

from .models import File
from files.forms import ZipfileUploadForm

# Create your views here.

class FileCreateView(CreateView):
    # template_name = 'files/file_create.html'
    model = File
    fields = ('name', 'file',)

class FileDetailView(DetailView):
    template_name = 'files/file_detail.html'
    model = File

class FileList(ListView):
    model = File

class ZipfileUploadView(FormView):
    template_name = 'files/upload-zipfile.html'
    form_class = ZipfileUploadForm
    success_url = '/files/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.process_zipfile()
        return super().form_valid(form)
