import _JCEHash

class SHA224Hash(_JCEHash.JCEHashWrapper):
    oid = '\x06\t`\x86H\x01e\x03\x04\x02\x04'
    digest_size = 28
    algname = "SHA224"

    def __init__(self, data=None):
        super(SHA224Hash, self).__init__("SHA-224")
        if data is not None:
            self.update(data)

def new(data=None):
    return SHA224Hash(data)

digest_size = 28
algname = "SHA224"
