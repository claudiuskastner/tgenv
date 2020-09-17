import click
import sys
import logging
import configparser
import os
import re
from git_wrapper import *
from version_handler import has_version, add_version, install_version
try:
    github_token = os.environ["GITHUB_TOKEN"]
except KeyError as ex:
    github_token = ""


logger = logging.getLogger(__name__)

config = configparser.ConfigParser()
configuration_path = os.path.join(os.path.dirname(__file__), "res/default.conf")
config.read(configuration_path)

help_content = f"\b" + config["DEFAULT"]["help"]

@click.group(help=help_content)
@click.pass_context
@click.option("-v", "--verbose", default=False, is_flag=True, help=config["DEFAULT"]["verbose"])
@click.option("-q", "--quiet", default=False, is_flag=True, help=config["DEFAULT"]["quiet"])
def cli(ctx, verbose, quiet):
    """[summary]

    :param ctx: [description]
    :type ctx: [type]
    :param verbose: [description]
    :type verbose: [type]
    :param quiet: [description]
    :type quiet: [type]
    """
    ctx.obj = {}

    ctx.verbose = verbose
    ctx.quiet = quiet
    if quiet:
        logger.setLevel(logging.NOTSET)
    elif verbose:
        logger.setLevel(logging.DEBUG)
    else:
        print("Loglevel info")
        logger.setLevel(logging.INFO)


@click.command(help=config["DEFAULT"]["get_remote_help"])
@click.pass_context
@click.option("-c", "--count", type=click.INT, default=10, help=config["DEFAULT"]["remote_version_count"])
def list_remote(ctx, count):
    get_versions(config["DEFAULT"]["tg_repository"], github_token, count=count)

def get_local_version():
    pass

@click.command(help=config["DEFAULT"]["get_remote_help"])
@click.pass_context
@click.argument("version", type=click.STRING)
def install(ctx, version):
    if re.match(r'v+[0-9]+\.[0-9]+\.+[0-9]*', version):
        if not has_version(config["DEFAULT"]["VERSION_FILE"], version):
            # try:
            get_release_asset(config["DEFAULT"]["tg_repository"], version, github_token)
            add_version(version, "versions/"+ version, config["DEFAULT"]["VERSION_FILE"])
            # except Exception as ex:
            #     print(ex)
        else:
            logging.info("Version already installed")
    else:
        logging.error("Not a valid version format")

@click.command(help=config["DEFAULT"]["get_remote_help"])
@click.argument("version", type=click.STRING)
@click.pass_context
def use(ctx, version):
    if re.match(r'v+[0-9]+\.[0-9]+\.+[0-9]*', version):
        if has_version(config["DEFAULT"]["VERSION_FILE"], version):
            install_version(config["DEFAULT"]["BINARY_TARGET"], "tgenv/versions/" ,version)

cli.add_command(list_remote)
cli.add_command(install)
cli.add_command(use)

if __name__ == "__main__":
    cli()
