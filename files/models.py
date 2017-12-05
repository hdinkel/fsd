from django.db import models
import hashlib

# Create your models here.

class File(models.Model):
    name = models.CharField(max_length=200, primary_key=True, unique=True)
    hash = models.CharField(max_length=200, unique=True)
    file = models.FileField() # TODO: add something like this: upload_to='documents/%Y/'); also use username?
    filesize = models.IntegerField(blank = True, null = True, editable = False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def save(self, *args, **kwargs):
        super(File, self).save(*args, **kwargs)
        self.filesize = self.file.size
        f = self.file.open('rb')
        hash = hashlib.sha256()
        if f.multiple_chunks():
           for chunk in f.chunks():
              hash.update(chunk)
        else:
              hash.update(f.read())
        f.close()
        self.hash =  hash.hexdigest()
        super(File, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
