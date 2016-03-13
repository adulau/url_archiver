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

# How are the URLs content stored?

url_archiver use the filesystem to store the content of a page. The path is defined by the SHA1 hash of the normalized URLs:

~~~
/tmp/.url_archiver/fee9bab3a6bd3061bf39ad79413ad8882e93395d
~~~

Two files are created ''archive'' and ''meta''. ''archive'' is the raw content of the web pages (if the HTTP return-code is 200). ''meta'' is the meta-data returned by the server including the requested URL in JSON format. The url_archiver namespace is used by url_archiver itself.

~~~json
{
  "X-GitHub-Request-Id": "B91F1118:3EEE:431A767:56E56D73",
  "Connection": "keep-alive",
  "url_archiver:url": "http://www.misp-project.org/",
  "Content-Type": "text/html; charset=utf-8",
  "url_archiver:urlhash": "fee9bab3a6bd3061bf39ad79413ad8882e93395d",
  "url_archiver:version": "0.1",
  "Date": "Sun, 13 Mar 2016 15:30:32 GMT",
  "X-Cache": "MISS",
  "Expires": "Sun, 13 Mar 2016 13:48:59 GMT",
  "X-Timer": "S1457883032.666525,VS0,VE118",
  "Server": "GitHub.com",
  "X-Fastly-Request-ID": "f0dbe5760cbd87d92666879afcd800a9faeadaaf",
  "Last-Modified": "Sun, 21 Feb 2016 21:26:59 GMT",
  "X-Cache-Hits": "0",
  "Accept-Ranges": "bytes",
  "X-Served-By": "cache-fra1236-FRA",
  "Access-Control-Allow-Origin": "*",
  "Vary": "Accept-Encoding",
  "Content-Length": "8609",
  "Content-Encoding": "gzip"
}
~~~
