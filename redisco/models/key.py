from __future__ import absolute_import

import six

try:
    six.text_type
except NameError:
    # Python 3
    six.string_types = six.text_type = str


class Key(six.text_type):
    def __getitem__(self, key):
        return Key(u"%s:%s" % (self, key))
