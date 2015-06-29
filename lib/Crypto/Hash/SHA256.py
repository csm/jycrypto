import _JCEHash

__doc__ = "SHA-256"

class SHA256Hash(_JCEHash.JCEHashWrapper):
    oid = '\x06\t`\x86H\x01e\x03\x04\x02\x01'
    digest_size = 32
    algname = "SHA256"

    def __init__(self, data=None):
        super(SHA256Hash, self).__init__("SHA-256")
        if data is not None:
            self.update(data)

def new(data=None):
    return SHA256Hash(data)

digest_size = 32
algname = "SHA256"
