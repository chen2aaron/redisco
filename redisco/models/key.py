try:
    unicode
except NameError:
    # Python 3
    basestring = unicode = str

class Key(unicode):
    def __getitem__(self, key):
        if isinstance(key, bytes):
            key = unicode(key, 'u8')
        return Key(u"%s:%s" % (self, key))
