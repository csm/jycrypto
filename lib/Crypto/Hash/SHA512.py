import _JCEHash

class SHA512Hash(_JCEHash.JCEHashWrapper):
    oid = '\x06\t`\x86H\x01e\x03\x04\x02\x03'
    digest_size = 64

    def __init__(self, data=None):
        super(SHA512Hash, self).__init__("SHA-512")
        if data is not None:
            self.update(data)

def new(data=None):
    return SHA512Hash(data)

digest_size = 64
