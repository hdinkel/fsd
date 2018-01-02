import zipfile
import tempfile
import os
import shutil
# from django.contrib.admin.models import LogEntry, ADDITION
# from django.contrib.contenttypes.models import ContentType
# from django.utils.encoding import force_text
from fsd.settings import MEDIA_ROOT
from .models import File
from .models import create_hash


def extract_zipfile(filename, username, project):
    """
    Extract all files of a given zipfile into a tempdirectory
    and generate a Files object of each file.
    """
    z = zipfile.ZipFile(filename)
    with tempfile.TemporaryDirectory(dir=MEDIA_ROOT) as tmpdirname:
        print("TmpDirName:", tmpdirname)
        for file in z.namelist():
            print("---")
            print("File2Extract:", file)
            # TODO: use ZipInfo Objects to get original file dates
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
                        f = File(file=tmpfilename, name=file, project=project, comment = "bundled upload via zipfile '{}'".format(filename))
                        f.save()

# Throws error:
#                        LogEntry.objects.log_action(
#                            user_id         = username,
#                            content_type_id = ContentType.objects.get_for_model(f).pk,
#                            object_id       = f,
#                            object_repr     = force_text(f),
#                            action_flag     = ADDITION
#                        )

                        dstdir = os.path.dirname(tmpfilename.replace(tmpdirname, MEDIA_ROOT))
                        print(dstdir)
                        if not os.path.isdir(dstdir):
                            os.makedirs(dstdir)
                        shutil.copy2(tmpfilename, dstdir)
                        # TODO: file = dstdir
#                except Exception:
                    # TODO catch hash collisions (also empty files produce collisions)
#                    pass
