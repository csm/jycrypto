import _JCECipher
import blockalgo

def new(key, mode=blockalgo.MODE_ECB, iv=None, **kwargs):
    if mode == blockalgo.MODE_CTR:
        if 'counter' not in kwargs:
            raise TypeError('counter argument is required')
        return _JCECipher.JCECTRCipher("RC4", mode, key, kwargs['counter'])
    if iv is not None and mode != blockalgo.MODE_ECB and len(iv) != block_size:
        raise ValueError('IV must be equal in length to the block size')
    return _JCECipher.JCECipherWrapper("RC4", mode, key, iv)

block_size = 1
