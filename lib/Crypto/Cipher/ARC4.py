from _JCECipher import JCECipherWrapper

def new(key, *args, **kwargs):
    return JCECipherWrapper("ARCFOUR", None, key)

block_size = 1
key_size = xrange(1, 257)
