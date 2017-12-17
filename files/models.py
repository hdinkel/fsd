from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
import os
import hashlib
import uuid

def hash_upload(instance, filename):
    """
    Function to rename a file to its filename plus sha256 hash
    This takes an instance and it's filename, computes the hash and combines
    the hash and filename to something like:
        Screenshot.png -> Screenshot__9876a786j694c28897347987.png
    """
    instance.file.open()  # make sure we're at the beginning of the file
    contents = instance.file.read()  # get the contents
    fname, ext = os.path.splitext(filename)
    return "{0}__{1}{2}".format(fname, create_hash(contents), ext)  # assemble the filename using a hash

def create_hash(data):
    """
    calculate sha256 hash function on given data
    >>> create_hash("testdata")
    ce41e5246ead8bddd2a2b5bbb863db250f328be9dc5c3041481d778a32f8130d
    """
    hash = hashlib.sha256()
    hash.update(data)
    return hash.hexdigest()

# Create your models here.


PROJECT_TYPES = (
                ('1', 'Publication'),
                ('2', 'Thesis'),
                ('3', 'Collaboration'),
                ('9', 'Other'),
                )
class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=400, blank=False, unique=False)
    owner = models.ForeignKey(get_user_model(), blank=True, on_delete=models.CASCADE,)
    project_type = models.CharField(max_length=100, blank=False, unique=False, choices=PROJECT_TYPES, default=1)
    description = models.TextField(max_length=400, unique=False, blank=True,)

    def __str__(self):
        return "{}".format(self.name)

class FileType(models.Model):
    id = models.AutoField(primary_key=True)
    filetype = models.CharField(max_length=100, blank=False, unique=False)
    ext = models.CharField(max_length=10, blank=True, unique=False)

    def __meta__(self):
        unique_together = (("filetype", "ext"),)

    def __str__(self):
        return "{} ({})".format(self.filetype, self.ext)


class File(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, unique=False)
    project = models.ForeignKey(Project, default=1, on_delete=models.CASCADE,)
    file = models.FileField(upload_to=hash_upload,)  # TODO: add something like this: upload_to='documents/%Y/'); also use username?
    filetype = models.ForeignKey(FileType, default=1, on_delete=models.CASCADE,)
    description = models.TextField(max_length=200, unique=False, blank=True,)
    comment = models.TextField(max_length=200, unique=False, blank=True, help_text='For internal use only...')
    hash = models.CharField(max_length=200, unique=True, editable=False, help_text='Auto-Generated SHA256 Hash (based on file content)')
    uuid = models.CharField(max_length=200, default=uuid.uuid4, unique=True, editable=False, help_text='Auto-Generated random unique ID')
    filesize = models.IntegerField(blank=True, null=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def generate_hash(self):
        contents = self.file.read()  # get the contents
        self.hash = create_hash(contents)

    def save(self, *args, **kwargs):
        self.generate_hash()
#        super(File, self).save(*args, **kwargs)
        self.filesize = self.file.size
        if self.name == '':
            self.name = self.file.name
        super(File, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('file_detail', args=[str(self.id)])
