from setuptools import setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    lice = f.read()

setup(
    name="tgenv",
    version="1.0.1",
    install_requires=["click", "requests", "tqdm", "PyGithub"],
    description="A tool for managing terragrunt versions",
    url="https://gitlab.com/claudiuskastner/tgenv",
    author="Claudius Kastner",
    keywords="terragrunt terraform versioning",
    long_description=readme,
    license=lice,
    author_email="claukast@gmail.com",
    data_files=[('config', ['tgenv/res/default.conf', 'tgenv/res/quotes'])],
    python_requires='>=3.8',
    include_package_data=True,
    packages=["tgenv"],
    entry_points={
        "console_scripts": [
            "tgenv=tgenv.main:cli",
        ]
    }
)
