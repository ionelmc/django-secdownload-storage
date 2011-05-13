# encoding: utf-8
from setuptools import setup, find_packages

import os

setup(
    name = "django-secdownload-storage",
    version = "0.1.0",
    url = 'https://bitbucket.org/ionelmc/django-secdownload-storage',
    download_url = '',
    license = 'BSD',
    description = """Django storage backend that can be used to serve files via lighttpd's mod_secdownload module. This 
storage backend is an extension to the reqular FileSystemStorage that will generate proper signed 
download urls.""",
    long_description = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    author = 'Ionel Mărieș Cristian',
    author_email = 'ionel.mc@gmail.com',
    packages = find_packages(),
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
