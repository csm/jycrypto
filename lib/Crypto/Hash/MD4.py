import _JCEHash

class MD4Hash(_JCEHash.JCEHashWrapper):
    oid = '\x06\x08*\x86H\x86\xf7\r\x02\x04'
    digest_size = 16

    def __init__(self, data=None):
        super(MD4Hash, self).__init__("MD4")
        if data is not None:
            self.update(data)

def new(data=None):
    return MD4Hash(data)

digest_size = 16
