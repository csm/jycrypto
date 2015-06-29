def strxor(a, b):
    return ''.join(map(lambda x: chr(ord(x[0]) ^ ord(x[1])), zip(a, b)))

def strxor_c(s, c):
    return ''.join(map(lambda x: chr(ord(x) ^ ord(c)), s))
