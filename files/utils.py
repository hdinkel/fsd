import zipfile
import tempfile
import os
import shutil
from fsd.settings import MEDIA_ROOT
from .models import File


def extract_zipfile(filename, username, project):
    """
    Extract all files of a given zipfile into a tempdirectory
    and generate a Files object of each file.
    """
    z = zipfile.ZipFile(filename)
    print("Username:", username)
    print("project:", project)
    with tempfile.TemporaryDirectory(dir=MEDIA_ROOT) as tmpdirname:
        print("TmpDirName:", tmpdirname)
        for file in z.namelist():
            print("File2Extract:", file)
            z.extract(file, tmpdirname)
            tmpfilename = os.path.join(tmpdirname, file)
            print("TmpFileName:", tmpfilename)
            if os.path.isfile(tmpfilename):
#                try:
                    f = File.objects.create(file=tmpfilename, name=file)
                    f.comment = "bundled upload via zipfile {}".format(filename)
                    f.save()
                    if '/' in tmpfilename:
                        shutil.copytree(tmpfilename, MEDIA_ROOT)
                    else:
                        shutil.copy2(tmpfilename, MEDIA_ROOT)
#                except Exception:
                    # TODO catch hash collisions (also empty files produce collisions)
#                    pass
