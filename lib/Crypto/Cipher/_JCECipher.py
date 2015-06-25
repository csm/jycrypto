from javax.crypto import Cipher as JCECipher
from javax.crypto.spec import SecretKeySpec, IvParameterSpec

class JCECipherWrapper(object):
    def __init__(self, alg, mode, key, iv=None):
        keyspec = SecretKeySpec(key, alg)
        self.__keysize = len(key)
        if mode is None and iv is None:
            self.__cryptor = JCECipher.getInstance(alg)
            self.__cryptor.init(JCECipher.ENCRYPT_MODE, keyspec)
            self.__cryptor = JCECipher.getInstance(alg)
            self.__cryptor.init(JCECipher.DECRYPT_MODE, keyspec)
        else:
            ivspec = IvParameterSpec(iv)
            self.__cryptor = JCECipher.getInstance(alg + "/" + mode)
            self.__cryptor.init(JCECipher.ENCRYPT_MODE, keyspec, ivspec)
            self.__decryptor = JCECipher.getInstance(alg + "/" + mode)
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
