# url_archiver

url_archiver is a simple library to fetch and archive URL on the file-system.

# How to install it?

~~~
pip install url_archiver
~~~

or from the source

~~~
git clone https://github.com/adulau/url_archiver.git
cd url_archiver
python3 setup.py build
sudo python3 setup.py install
~~~

# How to use url_archiver?

~~~python
#!/usr/bin/env python

from url_archiver import url_archiver

urlstoarchive = ['http://www.foo.be/', 'http://www.misp-project.org/']
archive_path = '/tmp/'
archiver = url_archiver.Archive(archive_path=archive_path)

# archive a set of urls
for url in urlstoarchive:
    archiver.fetch(url=url)

# return the content of the cache (if already fetched) or return the live
# content
print (archiver.fetch(url='http://www.foo.be/'))
~~~
