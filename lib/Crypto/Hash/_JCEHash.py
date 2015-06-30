from java.security import MessageDigest
from itertools import imap
import jarray
from Crypto.Util._str2bytes import _str2bytes

"""
JCA MessageDigest wrapper
"""
class JCEHashWrapper(object):
    """
    JCA MessageDigest wrapper.
    """

    def __init__(self, alg=None):
        if alg is not None:
            self.name = alg
            self.__hash = MessageDigest.getInstance(alg)

    def new(self, data=None):
        ret = JCEHashWrapper(self.__hash.getAlgorithm())
        if data is not None:
            ret.update(data)
        return ret

    def copy(self):
        copy = JCEHashWrapper()
        copy.__hash = self.__hash.clone()
        copy.name = copy.__hash.getAlgorithm()
        return copy

    def digest(self):
        # JCA resets the hash when you call digest(), pycrypto does not.
        copy = self.__hash.clone()
        return copy.digest().tostring()

    def hexdigest(self):
        return ''.join(map(lambda b: '%02x' % ord(b), self.digest()))

    def update(self, data):
        self.__hash.update(_str2bytes(data))

