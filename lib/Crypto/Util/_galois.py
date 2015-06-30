from struct import pack

def gcm_rightshift(vec):
    for x in range(15, 0, -1):
        c = vec[x] >> 1
        c |= (vec[x-1] << 7) & 0x80
        vec[x] = c
    vec[0] >>= 1
    return vec

def gcm_gf_mult(a, b):
    mask = [ 0x80, 0x40, 0x20, 0x10, 0x08, 0x04, 0x02, 0x01 ]
    poly = [ 0x00, 0xe1 ]

    Z = [0] * 16
    V = [c for c in a]

    for x in range(128):
        if b[x >> 3] & mask[x & 7]:
            Z = [V[y] ^ Z[y] for y in range(16)]
        bit = V[15] & 1
        V = gcm_rightshift(V)
        V[0] ^= poly[bit]
    return Z

def ghash(data, auth_data, h):
    u = (16 - len(data)) % 16
    v = (16 - len(auth_data)) % 16

    x = auth_data + chr(0) * v + data + chr(0) * u
    x += pack('>QQ', len(auth_data) * 8, len(data) * 8)

    y = [0] * 16
    vec_h = [ord(c) for c in h]

    for i in range(0, len(x), 16):
        block = [ord(c) for c in x[i:i+16]]
        y = [y[j] ^ block[j] for j in range(16)]
        y = gcm_gf_mult(y, vec_h)

    return ''.join(chr(c) for c in y)

def ghash_expand(s):
    return s
