from django.views.generic import DetailView, ListView, CreateView
from .models import File

# Create your views here.

class FileCreateView(CreateView):
    #template_name = 'files/file_create.html'
    model = File
    fields = ('name', 'file',)

class FileDetailView(DetailView):
    template_name = 'files/file_detail.html'
    model = File

class FileList(ListView):
    model = File
