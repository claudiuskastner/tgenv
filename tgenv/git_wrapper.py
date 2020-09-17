import os
import requests

from github import Github

from asset_downloader import download_asset

def get_versions(repository, git_token="", count=10):
    if git_token:
        github = Github(git_token)
    else:
        github = Github()
    repo = github.get_repo(repository)
    releases = repo.get_releases()
    for release in releases[:count]:
        print(release.tag_name)

def get_release_asset(repository, release_name, git_token=""):
    if git_token:
        github = Github(git_token)
    else:
        github = Github()
    repo = github.get_repo(repository)
    release = repo.get_release(release_name)
    assets = release.get_assets()
    for asset in assets:
        if asset.name == "terragrunt_linux_amd64":
            linux_amd64_asset = asset
            break
    url = linux_amd64_asset.browser_download_url
    download_asset(url, "tgenv/versions/" + release_name, git_token)
