import os
import sys
import stat
import shutil
import platform

def write_version(file_path: str, versions: str):
    """ Writes local available versions to a file

    :param file_path: Path to the destination file
    :type file_path: str
    :param versions: Content to write
    :type versions: str
    """
    with open(file_path, 'w') as version_file:
        version_file.write(versions)

def read_versions(file_path: str) -> str:
    """ Gets the content of a file
    """
    versions = ""
    with open(file_path, 'r') as version_file:
        versions = version_file.read()
    return versions

def version_file_exists(file_path: str) -> bool:
    """ Checks if the file exists
    """
    if os.path.isfile(file_path):
        return True
    raise FileNotFoundError

def copy_file(source: str, dest: str) -> bool:
    """ Copies a file from dest to source and gives executable rights
    """
    abs_path =  os.path.expanduser(dest)
    if not os.path.isfile(abs_path):
        with open(abs_path, "w") as file:
            file.write("")
    shutil.copyfile(source, abs_path)
    perm_state = os.stat(abs_path)
    os.chmod(abs_path, perm_state.st_mode | stat.S_IXUSR)

def check_files(path: str, version_file: str):
    """ Checks if the file structure is present and creates it if not

    :param path: Path to the dest folder
    :type path: str
    """
    versions_folder = os.path.expanduser(path + "versions")
    versions_file = os.path.expanduser(path + version_file)

    if not os.path.exists(versions_folder):
        os.makedirs(versions_folder)

    if not os.path.exists(versions_file):
        with open(versions_file, 'w') as ver_file:
            ver_file.write("{}")

def check_for_wsl() -> int:
    """ Checks if running on wsl
    """
    if os.path.exists("/mnt/c/Windows") or sys.platform != "linux":
        return 1
    elif platform.system():
        return 2
    return 2
