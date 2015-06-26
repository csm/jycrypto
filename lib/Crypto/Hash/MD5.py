import _JCEHash

class MD5Hash(_JCEHash.JCEHashWrapper):
    oid = '\x06\x08*\x86H\x86\xf7\r\x02\x05'
    digest_size = 16

    def __init__(self, data=None):
        super(MD5Hash, self).__init__("MD5")
        if data is not None:
            self.update(data)

def new(data=None):
    return MD5Hash(data)

digest_size = 16
