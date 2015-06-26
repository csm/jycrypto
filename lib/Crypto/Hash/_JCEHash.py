from java.security import MessageDigest

class JCEHashWrapper(object):
    def __init__(self, alg=None):
        if alg is not None:
            self.__hash = MessageDigest.getInstance(alg)

    def copy(self):
        copy = JCEHashWrapper()
        copy.__hash = self.__hash.clone()
        return copy

    def digest(self):
        return self.__hash.digest().tostring()

    def hexdigest(self):
        return ''.join(map(lambda b: '%02x' % ord(b), self.digest()))

    def update(self, data):
        self.__hash.update(data)
