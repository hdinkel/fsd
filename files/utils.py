import zipfile
import tempfile
import os
import shutil
from fsd.settings import MEDIA_ROOT
from .models import File
from .models import create_hash


def extract_zipfile(filename, username, project):
    """
    Extract all files of a given zipfile into a tempdirectory
    and generate a Files object of each file.
    """
    z = zipfile.ZipFile(filename)
#    print("Username:", username)
#    print("project:", project)
    with tempfile.TemporaryDirectory(dir=MEDIA_ROOT) as tmpdirname:
        print("TmpDirName:", tmpdirname)
        for file in z.namelist():
            print("File2Extract:", file)
            z.extract(file, tmpdirname)
            tmpfilename = os.path.join(tmpdirname, file)
            print("TmpFileName:", tmpfilename)
            if os.path.isfile(tmpfilename):
#                try:
                    with open(tmpfilename,'rb') as file2hash:
                        hash = create_hash(file2hash.read())
                        print(hash)
                    try:
                        f = File.objects.get(hash = hash)
                        print("File {} with the following hash already exists in DB: '{}'".format(f.id, hash))
                    except File.DoesNotExist:
                        f = File.objects.create(file=tmpfilename, name=file)
                        f.comment = "bundled upload via zipfile {}".format(filename)
                        print(f.hash)
                        print(f.generate_hash())
                        f.save()
                        shutil.copy(tmpfilename, MEDIA_ROOT)
#                except Exception:
                    # TODO catch hash collisions (also empty files produce collisions)
#                    pass
