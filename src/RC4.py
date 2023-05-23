def KSA(key):
    key_length = len(key)
    # Initialize S as a list of integers from 0 to 255
    S = list(range(256))                 
    j = 0

    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        # Swap values
        S[i], S[j] = S[j], S[i]          # Swap values

    return S

def PRGA(S):
    i = 0
    j = 0

    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
         # Swap values
        S[i], S[j] = S[j], S[i]         
        K = S[(S[i] + S[j]) % 256]
        yield K


# executing the XOr between the text and keystream
def RC4(text, keystream):
    res = []

    for c in text:
        val = c ^ next(keystream)
        res.append(val)

    output_text = ''.join(map(chr, res))
    return output_text 