# -*- coding: utf-8 -*-

import os
import uuid

from django.core.files.storage import default_storage


def random_upload_path(instance, filename):
    """ Dynamic path to logo path, based on company slug. """
    basename, extension = os.path.splitext(filename)
    while True:
        random = uuid.uuid4().hex + extension
        path = os.path.join(unicode(instance._meta), random)
        if not default_storage.exists(path):
            break
    return path