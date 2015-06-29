import _JCEHash

__doc__ = "MD2"

class MD2Hash(_JCEHash.JCEHashWrapper):
    oid = '\x06\x08*\x86H\x86\xf7\r\x02\x02'
    digest_size = 16
    algname = "MD2"

    def __init__(self, data=None):
        super(MD2Hash, self).__init__(algname)
        if data is not None:
            self.update(data)

def new(data=None):
    return MD2Hash(data)

digest_size = 16
algname = "MD2"
