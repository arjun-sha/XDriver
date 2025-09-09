import os
from setuptools import find_packages, setup

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Version
with open(os.path.join(BASE_DIR, "VERSION.txt")) as f:
    version = f.read().strip()

# Read requirements.txt
with open(os.path.join(BASE_DIR, "requirements.txt")) as f:
    requirements = f.read().splitlines()

# Readme
with open(os.path.join(BASE_DIR, "README.md")) as f:
    readme = f.read()

setup(
    name="x_driver",
    version="1.0.1",
    author="Arjun Shankar",
    author_email="arjun.sha2425@gmail.com",
    description="Patched playwright driver for block free web scraping!",
    long_description=readme,
    license="Apache-2.0",
    packages=find_packages(),
    include_package_data=True,
    package_data={"x_driver": ["bundle/**/*"]},
    long_description_content_type="text/markdown",
    install_requires=requirements,
    keywords=["Playwright", "Cloudflare", "Kasada", "Datadome"],
    entry_points={"console_scripts": ["x_driver=x_driver.__main__:activator"]},
)
