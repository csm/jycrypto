import _JCECipher
import blockalgo

def new(key, mode=blockalgo.MODE_ECB, iv=None, **kwargs):
    if mode == blockalgo.MODE_CTR:
        if 'counter' not in kwargs:
            raise TypeError('counter argument is required')
        return _JCECipher.JCECTRCipher("AES", mode, key, kwargs['counter'])
    if iv is not None and mode != blockalgo.MODE_ECB and len(iv) != block_size:
        raise ValueError('IV must be equal in length to the block size')
    return _JCECipher.JCECipherWrapper("AES", mode, key, iv)

#: Electronic Code Book (ECB). See `blockalgo.MODE_ECB`.
MODE_ECB = 1
#: Cipher-Block Chaining (CBC). See `blockalgo.MODE_CBC`.
MODE_CBC = 2
#: Cipher FeedBack (CFB). See `blockalgo.MODE_CFB`.
MODE_CFB = 3
#: This mode should not be used.
MODE_PGP = 4
#: Output FeedBack (OFB). See `blockalgo.MODE_OFB`.
MODE_OFB = 5
#: CounTer Mode (CTR). See `blockalgo.MODE_CTR`.
MODE_CTR = 6
#: OpenPGP Mode. See `blockalgo.MODE_OPENPGP`.
MODE_OPENPGP = 7
#: Counter with CBC-MAC (CCM) Mode. See `blockalgo.MODE_CCM`.
MODE_CCM = 8
#: EAX Mode. See `blockalgo.MODE_EAX`.
MODE_EAX = 9
#: Syntethic Initialization Vector (SIV). See `blockalgo.MODE_SIV`.
MODE_SIV = 10
#: Galois Counter Mode (GCM). See `blockalgo.MODE_GCM`.
MODE_GCM = 11
#: Size of a data block (in bytes)
block_size = 16
#: Size of a key (in bytes)
key_size = ( 16, 24, 32 )
