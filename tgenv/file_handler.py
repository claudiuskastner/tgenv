import os
import shutil
import stat

def write_version(file_path, versions):
    with open(file_path, 'w') as version_file:
        version_file.write(versions)

def read_versions(file_path):
    versions = ""
    with open(file_path, 'r') as version_file:
        versions = version_file.read()
    return versions

def version_file_exists(file_path):
    if os.path.isfile(file_path):
        return True
    else:
        raise FileNotFoundError

def copy_file(source, dest):
    abs_path =  os.path.expanduser(dest)
    shutil.copyfile(source, abs_path)
    os.chmod(abs_path, stat.S_IXUSR)

def purge_files(folder):
    pass
