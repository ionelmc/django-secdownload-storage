==========================
django-secdownload-storage
==========================

Django storage backend that can be used to serve files via lighttpd's mod_secdownload module. This 
storage backend is an extension to the reqular FileSystemStorage that will generate proper signed 
download urls.

Installation
------------

::

  pip install django-secdownload-storage
  
or::

  easy_install django-secdownload-storage

or via source checkout::

  hg clone https://bitbucket.org/ionelmc/django-secdownload-storage
  cd django-secdownload-storage
  python setup.py install

Usage 
-----

In your django models you should add ``storage=SecDownloadFileSystemStorage()`` to the fields you 
want served via secdownload. 

Required settings: ::

  SEC_DOWNLOAD_ENABLED = True
  SEC_DOWNLOAD_SECRET_KEY = 'VERYVERYSECRET'
  SEC_DOWNLOAD_MEDIA_URL = MEDIA_URL + 'dl/'

Example model: ::

  import secdownload_storage
  
  class Foo(models.Model):
    secret_picture = models.ImageField(upload_to='secret-pictures', storage=secdownload_storage.SecDownloadFileSystemStorage())

You need to enable mod_secdownload and have configuration similar to this (see 
http://redmine.lighttpd.net/wiki/1/Docs:ModSecDownload for more info): ::

  secdownload.secret = "VERYVERYSECRET"
  secdownload.document-root = "/path/to/media"
  secdownload.uri-prefix = "/dl/"
  secdownload.timeout = 3600
    
Also, note that you should disallow access to those files in the lighttpd configuration as they 
would be served with your regular media files. Eg: ::

  $HTTP["url"] =~ "^/media/secret-pictures" {
      url.access-deny = ("")
  }

Configuration
-------------

* SEC_DOWNLOAD_ENABLED - set this to False to disable signing the urls and generate them like 
  FileSystemStorage. This is useful for development (if you use django's devserver).
* SEC_DOWNLOAD_SECRET_KEY - this is the secret key that is used to sign the requests  
* SEC_DOWNLOAD_MEDIA_URL - this is the prefix path that's used instead of MEDIA_URL when 
  SEC_DOWNLOAD_ENABLED is set to True. If SEC_DOWNLOAD_ENABLED is set to False 
  SecDownloadFileSystemStorage will use MEDIA_URL for the prefix instead.