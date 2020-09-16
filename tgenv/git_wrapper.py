import os
import requests

from github import Github

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
    url = release.tarball_url
    release_asset = requests.get(url)
    with open("versions/" + release_name, 'wb') as release_file:
        release_file.write(release_asset.content)
    print(release)

# get_versions("gruntwork-io/terragrunt")
#get_release_asset("gruntwork-io/terragrunt", "v0.24.4")
