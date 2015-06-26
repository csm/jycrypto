from javax.crypto import Mac
from javax.crypto.spec import SecretKeySpec

class HMAC(object):
    digest_size = None

    def __init__(self, key, msg=None, digestmod=None):
        self.digest_size = 16
        alg = "HmacMD5"
        if digestmod is not None:
            alg = "Hmac" + digestmod.algname
            self.digest_size = digestmod.digest_size
        self.__keylen = len(key)
        self.__mac = Mac.getInstance(alg)
        keyspec = SecretKeySpec(key, alg)
        self.__mac.init(keyspec)
        if msg is not None:
            self.update(msg)

    def update(self, msg):
        self.__mac.update(msg)

    def copy(self):
        copy = HMAC('*' * self.__keylen)
        copy.__mac = self.__mac.clone()
        return copy

    def digest(self):
        return self.__mac.doFinal().tostring()

    def hexdigest(self):
        return ''.join(map(lambda b: '%02x' % ord(b), self.digest()))
