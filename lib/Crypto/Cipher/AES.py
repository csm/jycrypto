import _JCECipher

def new(key, *args, **kwargs):
    mode = None
    if args[0] == MODE_ECB:
        mode = "ECB/NoPadding"
    elif args[0] == MODE_CBC:
        mode = "CBC/NoPadding"
    elif args[0] == MODE_CFB:
        mode = "CFB/NoPadding"
    elif args[0] == MODE_PGP:
        raise ValueError('MODE_PGP is not supported')
    elif args[0] == MODE_OFB:
        mode = "OFB/NoPadding"
    elif args[0] == MODE_CTR:
        mode = "CTR/NoPadding"
    elif args[0] == MODE_OPENPGP:
        raise ValueError('MODE_OPENPGP is not yet implemented')
    else:
        raise ValueError('unknown mode: ' + args[0])
    return _JCECipher.JCECipherWrapper("AES", mode, key, args[1])

MODE_ECB = 1
MODE_CBC = 2
MODE_CFB = 3
MODE_PGP = 4
MODE_OFB = 5
MODE_CTR = 6
MODE_OPENPGP = 7
block_size = 16
key_size = (16, 24, 32)
