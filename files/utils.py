import zipfile
import tempfile
import os
from fsd.settings import MEDIA_ROOT
from .models import File


def extract_zipfile(zippedfile):
    """
    Extract all files of a given zipfile into a tempdirectory
    and generate a Files object of each file.
    """
    z = zipfile.ZipFile(zippedfile)
    print(os.getcwd())
    with tempfile.TemporaryDirectory(dir=MEDIA_ROOT) as tmpdirname:
        print(tmpdirname)
        for file in z.namelist():
            print(file)
            z.extract(file, tmpdirname)
            tmpfilename = os.path.join(tmpdirname, file)
            print(tmpfilename)
            os.popen('ls -lah ' + tmpdirname)
            if os.path.isfile(tmpfilename):
                f = File.objects.create(file=tmpfilename, name=file)
                f.save()


if __name__ == '__main__':
    extract_zipfile('/Users/dinkel/down/libraries.zip')
