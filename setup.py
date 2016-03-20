from setuptools import setup, find_packages
setup(
    name="urlarchiver",
    version="0.2",
    packages=find_packages(),
    install_requires=['requests', 'url-normalize'],
    author="Alexandre Dulaunoy",
    author_email="a@foo.be",
    description="url-archiver is a simple library to fetch and archive URL on the file-system.",
    license="AGPL",
    keywords="internet url caching webcache cache",
    url="http://github.com/adulau/url_archiver"
)
