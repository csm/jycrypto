from java.security import SecureRandom
import jarray
import threading

class _UserFriendlyRNG(object):
    def __init__(self):
        self.closed = False
        self.__securerandom = None
        self.reinit()

    def reinit(self):
        self.__securerandom = SecureRandom()

    def close(self):
        self.closed = True
        self.__securerandom = None

    def flush(self):
        pass

    def read(self, N):
        if self.closed:
            raise ValueError("I/O operation on closed file")
        if not isinstance(N, (long, int)):
            raise TypeError("an integer is required")
        if N < 0:
            raise ValueError("cannot read to end of infinite stream")

        result = jarray.zeros(N, 'b')
        self.__securerandom.nextBytes(result)
        return result.tostring()

class _LockingUserFriendlyRNG(_UserFriendlyRNG):
    def __init__(self):
        self._lock = threading.Lock()
        _UserFriendlyRNG.__init__(self)

    def close(self):
        self._lock.acquire()
        try:
            return _UserFriendlyRNG.close(self)
        finally:
            self._lock.release()

    def reinit(self):
        self._lock.acquire()
        try:
            return _UserFriendlyRNG.reinit(self)
        finally:
            self._lock.release()

    def read(self, bytes):
        self._lock.acquire()
        try:
            return _UserFriendlyRNG.read(self, bytes)
        finally:
            self._lock.release()

class RNGFile(object):
    def __init__(self, singleton):
        self.closed = False
        self._singleton = singleton

    # PEP 343: Support for the "with" statement
    def __enter__(self):
        """PEP 343 support"""
    def __exit__(self):
        """PEP 343 support"""
        self.close()

    def close(self):
        # Don't actually close the singleton, just close this RNGFile instance.
        self.closed = True
        self._singleton = None

    def read(self, bytes):
        if self.closed:
            raise ValueError("I/O operation on closed file")
        return self._singleton.read(bytes)

    def flush(self):
        if self.closed:
            raise ValueError("I/O operation on closed file")

_singleton_lock = threading.Lock()
_singleton = None
def _get_singleton():
    global _singleton
    _singleton_lock.acquire()
    try:
        if _singleton is None:
            _singleton = _LockingUserFriendlyRNG()
        return _singleton
    finally:
        _singleton_lock.release()

def new():
    return RNGFile(_get_singleton())

def reinit():
    _get_singleton().reinit()

def get_random_bytes(n):
    """Return the specified number of cryptographically-strong random bytes."""
    return _get_singleton().read(n)
