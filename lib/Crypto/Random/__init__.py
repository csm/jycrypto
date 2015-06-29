__all__ = ['new']

from Crypto.Random import _UserFriendlyRNG

def new(*args, **kwargs):
    """Return a file-like object that outputs cryptographically random bytes."""
    return _UserFriendlyRNG.new(*args, **kwargs)

def get_random_bytes(n):
    """Return the specified number of cryptographically-strong random bytes."""
    return _UserFriendlyRNG.get_random_bytes(n)
