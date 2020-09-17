import json
import os

from file_handler import read_versions, version_file_exists, write_version, copy_file

def get_local_versions(filepath):
    versions = read_versions(filepath)
    versions = json.loads(versions)
    return versions

def add_version(version, filepath, version_file):
    versions = get_local_versions(version_file)
    versions[version] = "versions/" + version
    write_version(version_file, json.dumps(versions))

def get_version_path(version):
    pass

def parse_versions(filepath):
    pass

def has_version(filepath, version):
    versions = get_local_versions(filepath)
    try:
        version_file_exists(versions[version])
        return True
    except FileNotFoundError:
        return False
    except KeyError:
        return False

def install_version(target_path, source_path, version):
    copy_file(source_path + version, target_path)
