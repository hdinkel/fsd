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
            print("---")
            print("File2Extract:", file)
            z.extract(file, tmpdirname)
            tmpfilename = os.path.join(tmpdirname, file)
            print("TmpFileName:", tmpfilename)
            if os.path.isfile(tmpfilename):
#                try:
                    with open(tmpfilename,'rb') as file2hash:
                        hash = create_hash(file2hash.read())
                    try:
                        f = File.objects.get(hash = hash)
                        print("File {} with the following hash already exists in DB: '{}'".format(f.id, hash))
                    except File.DoesNotExist:
                        print('file:', file)
                        f = File(file=tmpfilename, name=file, comment = "bundled upload via zipfile {}".format(filename))
                        f.save()
                        dstdir = os.path.dirname(tmpfilename.replace(tmpdirname, MEDIA_ROOT))
                        print(dstdir)
                        if not os.path.isdir(dstdir):
                            os.makedirs(dstdir)
                        shutil.copy2(tmpfilename, dstdir)
#                except Exception:
                    # TODO catch hash collisions (also empty files produce collisions)
#                    pass
