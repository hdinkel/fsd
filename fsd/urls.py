"""fsd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from files.views import FileList
from files.views import FileDetailView
from files.views import FileCreateView
from files.views import upload_zipfile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('files/', FileList.as_view(), name="file_list"),
#    path('files/upload.zip', ZipfileUploadView.as_view(), name="upload-zipfile"),
    path('files/upload.zip', upload_zipfile, name="upload-zipfile"),
    path('files/<int:pk>/', FileDetailView.as_view(), name="file_detail"),
    path('files/<int:pk>/edit', FileCreateView.as_view(), name="file_edit"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

