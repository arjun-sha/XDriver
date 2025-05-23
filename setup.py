from setuptools import find_packages, setup

setup(
    name="x_driver",
    author="Arjun Shankar",
    author_email="arjun.sha2425@gmail.com",
    description="Patched playwright driver for block free web scraping!",
    long_description=open("README.md").read(),
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    long_description_content_type="text/markdown",
    install_requires=["colorlog"],
    keywords=["Playwright", "Cloudflare", "Kasada", "Datadome"],
    version=" ".join([i.strip() for i in open("VERSION.txt")]).strip(),
    entry_points={"console_scripts": ["x_driver=x_driver.__main__:activator"]}
)
