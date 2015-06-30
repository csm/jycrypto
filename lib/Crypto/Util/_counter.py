# Slow implementation of counters

from java.math import BigInteger
from itertools import imap
import jarray
from Crypto.Util._str2bytes import _str2bytes
import string
from Crypto.Util.number import bytes_to_long, long_to_bytes

class _CounterImpl(object):
    def __init__(self, initial, prefix, suffix, big_endian, wrap):
        if big_endian:
            self.counter = bytes_to_long(initial)
        else:
            self.counter = bytes_to_long(''.join(reversed(initial)))
        self.wrap = wrap
        self.max = bytes_to_long('\xff' * len(initial))
        self.length = len(initial)
        if prefix is None:
            self.prefix = ''
        else:
            self.prefix = prefix
        if suffix is None:
            self.suffix = ''
        else:
            self.suffix = suffix
        self.big_endian = big_endian

    def __call__(self, *args, **kwargs):
        if self.counter > self.max:
            if not self.wrap:
                raise OverflowError('counter overflow')
            self.counter = 0
        ret = long_to_bytes(self.counter, self.length)
        if len(ret) < self.length:
            ret = '\x00' * (self.length - len(ret)) + ret
        self.counter += 1
        if not self.big_endian:
            ret = ''.join(reversed(ret))
        return self.prefix + ret + self.suffix

    def next_value(self):
        if self.counter > self.max:
            if not self.wrap:
                raise OverflowError('counter overflow')
            self.counter = 0
        return self.counter

def _newBE(prefix, suffix, initval, allow_wraparound=0):
    return _CounterImpl(initval, prefix, suffix, True, allow_wraparound != 0)

def _newLE(prefix, suffix, initval, allow_wraparound=0):
    return _CounterImpl(initval, prefix, suffix, False, allow_wraparound != 0)
