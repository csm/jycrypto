import _JCEHash

__doc__ = "RIPEMD-160"

class RIPEMD160Hash(_JCEHash.JCEHashWrapper):
    oid = '\x06\x05+$\x03\x02\x01'
    digest_size = 20
    algname = "RIPEMD160"

    def __init__(self, data=None):
        super(RIPEMD160Hash, self).__init__(algname)
        if data is not None:
            self.update(data)

def new(data=None):
    return RIPEMD160Hash(data)

digest_size = 20
algname = "RIPEMD160"
