from Crypto.Util.strxor import strxor

def _extendseq(seq, pos, count):
    l = len(seq)
    for i in xrange(0, count):
        yield seq[(pos + i) % l]

class XORCipher(object):
    def __init__(self, key, *args, **kwargs):
        self.__pos = 0
        self.__key = key

    def encrypt(self, data):
        result = strxor(data, _extendseq(self.__key, self.__pos, len(data)))
        self.__pos += len(data)
        return result

    def decrypt(self, data):
        return self.encrypt(data)

def new(key, *args, **kwargs):
    return XORCipher(key, *args, **kwargs)

#: Size of a data block (in bytes)
block_size = 1
#: Size of a key (in bytes)
key_size = xrange(1,32+1)