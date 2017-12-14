from django.shortcuts import render
from django.views.generic import View, DetailView, TemplateView, ListView
from .models import File

# Create your views here.


class FileDetailView(DetailView):
    template_name = 'files/file_detail.html'
    model = File

class FileList(ListView):
    model = File
