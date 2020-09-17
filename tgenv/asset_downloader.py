from tqdm import tqdm
import requests
import math


def download_asset(url, out_file, github_token):
    header = {"Authorization": "token" + github_token}
    download_stream = requests.get(url, stream=True)

    size = int(download_stream.headers.get('content-length', 0));
    block_size = 1024
    written = 0
    with open(out_file, 'wb') as asset:
        for data in tqdm(download_stream.iter_content(block_size), total=math.ceil(size//block_size) , unit='KB', unit_scale=True):
            written = written  + len(data)
            asset.write(data)
    if size != 0 and written != size:
        raise DownloadException("")

class DownloadException(Exception):
    def __init__(self):
        Exception.__init__(self)
