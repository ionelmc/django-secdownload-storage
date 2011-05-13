import time
import hashlib
import urlparse

from django.core.files.storage import FileSystemStorage, filepath_to_uri
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

ENABLED = settings.SEC_DOWNLOAD_ENABLED

class SecDownloadFileSystemStorage(FileSystemStorage):
    def __init__(self, location=None, base_url=None, secret_key=None):
        if ENABLED:
            if base_url is None:
                base_url = settings.SEC_DOWNLOAD_MEDIA_URL
            if secret_key is None:
                secret_key = settings.SEC_DOWNLOAD_SECRET_KEY

            self.secret_key = secret_key
        super(self.__class__, self).__init__(location=location, base_url=base_url)

    def url(self, name):
        if ENABLED:
            file_path = filepath_to_uri(name)
            hextime = "%08x" % time.time()
            token = hashlib.md5(self.secret_key + '/' + file_path + hextime).hexdigest()
            return urlparse.urljoin(self.base_url, '/'.join((token, hextime, file_path)))
        else:
            return super(self.__class__, self).url(name)
