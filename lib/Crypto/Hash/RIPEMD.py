import _JCEHash

class RIPEMD160Hash(_JCEHash.JCEHashWrapper):
    oid = '\x06\x05+$\x03\x02\x01'
    digest_size = 20

    def __init__(self, data=None):
        super(RIPEMD160Hash, self).__init__("RIPEMD160")
        if data is not None:
            self.update(data)

def new(data=None):
    return RIPEMD160Hash(data)

digest_size = 20
