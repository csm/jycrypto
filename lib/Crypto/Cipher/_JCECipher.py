from javax.crypto import Cipher as JCECipher
from javax.crypto.spec import SecretKeySpec, IvParameterSpec
import blockalgo
from Crypto.Util.strxor import strxor

_modes = {}
_modes[blockalgo.MODE_ECB] = "/ECB/NoPadding"
_modes[blockalgo.MODE_CBC] = "/CBC/NoPadding"
_modes[blockalgo.MODE_CFB] = "/CFB/NoPadding"
_modes[blockalgo.MODE_OFB] = "/OFB/NoPadding"
_modes[blockalgo.MODE_CTR] = "/CTR/NoPadding"

class JCECipherWrapper(object):
    def __init__(self, alg, mode, key, iv=None):
        modestr = _modes.get(mode, "/ECB/NoPadding")
        keyspec = SecretKeySpec(key, alg)
        self.__keysize = len(key)
        self.IV = iv
        if iv is None or mode == blockalgo.MODE_ECB:
            if mode != blockalgo.MODE_ECB:
                raise ValueError('mode requires an IV')
            self.__cryptor = JCECipher.getInstance(alg + modestr)
            self.__cryptor.init(JCECipher.ENCRYPT_MODE, keyspec)
            self.__decryptor = JCECipher.getInstance(alg + modestr)
            self.__decryptor.init(JCECipher.DECRYPT_MODE, keyspec)
        else:
            ivspec = IvParameterSpec(iv)
            self.__cryptor = JCECipher.getInstance(alg + modestr)
            self.__cryptor.init(JCECipher.ENCRYPT_MODE, keyspec, ivspec)
            self.__decryptor = JCECipher.getInstance(alg + modestr)
            self.__decryptor.init(JCECipher.DECRYPT_MODE, keyspec, ivspec)

    def encrypt(self, plaintext):
        return self.__cryptor.update(plaintext).tostring()

    def decrypt(self, ciphertext):
        return self.__decryptor.update(ciphertext).tostring()

    def __get_blocksize(self):
        return self.__cryptor.getBlockSize()

    block_size = property(__get_blocksize)

    def __get_keysize(self):
        return self.__keysize

    key_size = property(__get_keysize)

class JCECTRCipher(JCECipherWrapper):
    def __init__(self, alg, mode, key, counter):
        super(JCECTRCipher, self).__init__(alg, blockalgo.MODE_ECB, key)
        self.IV = counter
        self.__counter = counter

    def encrypt(self, plaintext):
        return ''.join(map(lambda i: strxor(plaintext[i:i+self.block_size], super(JCECTRCipher, self).encrypt(self.__counter())), range(0, len(plaintext), self.block_size)))

    def decrypt(self, ciphertext):
        return self.encrypt(ciphertext)