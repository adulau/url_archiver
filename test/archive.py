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
