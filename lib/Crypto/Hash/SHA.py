import _JCEHash

class SHA1Hash(_JCEHash.JCEHashWrapper):
    oid = '\x06\x05+\x0e\x03\x02\x1a'
    digest_size = 20

    def __init__(self, data=None):
        super(SHA1Hash, self).__init__("SHA-1")
        if data is not None:
            self.update(data)

def new(data=None):
    return SHA1Hash(data)

digest_size = 20
