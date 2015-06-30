import jarray

def _long2byte(l):
    if l > 255:
        raise ValueError('out of range')
    elif l > 127:
        return -129 + (l - 127)
    else:
        return l

def _str2bytes(s):
    return jarray.array(map(_long2byte, map(ord, s)), 'b')

