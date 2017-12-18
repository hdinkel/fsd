from django.views.generic import DetailView, ListView, CreateView
from django.views.generic.edit import FormView
# from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import File
from .utils import extract_zipfile
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

# class ZipfileUploadView(FormView):
#     template_name = 'files/upload-zipfile.html'
#     form_class = ZipfileUploadForm
#     success_url = '/files/'
#
#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         form.process_zipfile()
#         return super().form_valid(form)

def upload_zipfile(request):
    if request.method == 'POST':
        form = ZipfileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES['file_field']
            # TODO Add try-except
            # TODO Add check for actual zipfile
            extract_zipfile(f)
            return HttpResponseRedirect('/files/')
    else:
        form = ZipfileUploadForm()
    return render(request, 'files/upload-zipfile.html', {'form': form})
