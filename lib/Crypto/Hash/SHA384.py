import _JCEHash

__doc__ = "SHA-384"

class SHA384Hash(_JCEHash.JCEHashWrapper):
    oid = '\x06\t`\x86H\x01e\x03\x04\x02\x02'
    digest_size = 48
    algname = "SHA384"

    def __init__(self, data=None):
        super(SHA384Hash, self).__init__("SHA-384")
        self.name = algname
        if data is not None:
            self.update(data)

def new(data=None):
    return SHA384Hash(data)

digest_size = 48
algname = "SHA384"
block_size = 128
