from django.db import models
from django.urls import reverse
import os
import hashlib
import uuid

# Create your models here.

def hash_upload(instance, filename):
    """
    Function to rename a file to its filename plus sha256 hash
    This takes an instance and it's filename, computes the hash and combines
    the hash and filename to something like:
        Screenshot.png -> Screenshot__9876a786j694c28897347987.png
    """
    instance.file.open() # make sure we're at the beginning of the file
    contents = instance.file.read() # get the contents
    fname, ext = os.path.splitext(filename)
    return "{0}__{1}{2}".format(fname, create_hash(contents), ext) # assemble the filename using a hash

def create_hash(data):
    """
    calculate sha256 hash function on given data
    >>> create_hash("testdata")
    ce41e5246ead8bddd2a2b5bbb863db250f328be9dc5c3041481d778a32f8130d
    """
    hash = hashlib.sha256()
    hash.update(data)
    return hash.hexdigest()

class FileType(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100, blank=False, unique=False)
    ext  = models.CharField(max_length=10, blank=False, unique=False)

class File(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, unique=False)
    uuid = models.CharField(max_length=200, default=uuid.uuid4, unique=True, editable=False)

#    description = models.CharField(max_length=200, default=uuid.uuid4, unique=True, editable=False)
#    comment = models.CharField(max_length=200, default=uuid.uuid4, unique=True, editable=False)
#    type = models.Foreignkey(FileType)

    file = models.FileField(upload_to=hash_upload,) # TODO: add something like this: upload_to='documents/%Y/'); also use username?
    hash = models.CharField(max_length=200, unique=True, editable=False)
    filesize = models.IntegerField(blank=True, null=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def generate_hash(self):
#        with self.file.open() as f: # make sure we're at the beginning of the file
        contents = self.file.read() # get the contents
        self.hash = create_hash(contents)

    def save(self, *args, **kwargs):
        self.generate_hash()
#        super(File, self).save(*args, **kwargs)
        self.filesize = self.file.size
        if self.name  == '':
            self.name = self.file.name
        super(File, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('file_detail', args=[str(self.id)])
