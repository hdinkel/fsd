from django.db import models
import os
import hashlib
import uuid

# Create your models here.

def hash_upload(instance, filename):
    instance.file.open() # make sure we're at the beginning of the file
    contents = instance.file.read() # get the contents
    fname, ext = os.path.splitext(filename)
    return "{0}__{1}{2}".format(fname, create_hash(contents), ext) # assemble the filename

def create_hash(data):
    hash = hashlib.sha256()
    hash.update(data)
    return hash.hexdigest()


class File(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, unique=False)
    uuid = models.CharField(max_length=200, default=uuid.uuid4, unique=True, editable=False)
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
