from django.db import models
import hashlib

# Create your models here.

class File(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, unique=False)
    hash = models.CharField(max_length=200, unique=True, editable=False)
    file = models.FileField() # TODO: add something like this: upload_to='documents/%Y/'); also use username?
    filesize = models.IntegerField(blank=True, null=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super(File, self).save(*args, **kwargs)
        self.filesize = self.file.size
        with self.file.open('rb') as f:
            hash = hashlib.sha256()
            if f.multiple_chunks():
                for chunk in f.chunks():
                    hash.update(chunk)
                else:
                    hash.update(f.read())
        self.hash =  hash.hexdigest()
        if self.name  == '':
#            self.name = f.name
            self.name = self.file.name
        super(File, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
