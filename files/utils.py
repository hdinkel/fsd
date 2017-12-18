import zipfile
import tempfile
import os
import shutil
from fsd.settings import MEDIA_ROOT
from .models import File


def extract_zipfile(zippedfile):
    """
    Extract all files of a given zipfile into a tempdirectory
    and generate a Files object of each file.
    """
    z = zipfile.ZipFile(zippedfile)
#    print(os.getcwd())
    with tempfile.TemporaryDirectory(dir=MEDIA_ROOT) as tmpdirname:
        print("TmpDirName:", tmpdirname)
        for file in z.namelist():
            print("File2Extract:", file)
            z.extract(file, tmpdirname)
            tmpfilename = os.path.join(tmpdirname, file)
            print("TmpFileName:", tmpfilename)
            if os.path.isfile(tmpfilename):
                try:
                    shutil.copy2(tmpfilename, MEDIA_ROOT)
                    f = File.objects.create(file=tmpfilename, name=file)
                    f.comment = "bundled upload via zipfile '{}'".format(zippedfile)
                    f.save()
                except Exception:
                    # TODO catch hash collisions (also empty files produce collisions)
                    pass

if __name__ == '__main__':
    extract_zipfile('/Users/dinkel/down/libraries.zip')
