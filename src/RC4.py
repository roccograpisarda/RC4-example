def KSA(key):
    key_length = len(key)
    S = list(range(256))                 # Initialize S as a list of integers from 0 to 255
    j = 0

    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]          # Swap values

    return S


def PRGA(S):
    i = 0
    j = 0

    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]          # Swap values
        K = S[(S[i] + S[j]) % 256]
        yield K

def RC4(key, text):
    # Generate the initial permutation of S based on the key
    S = KSA(key)
    # Generate the keystream using the modified S
    keystream = PRGA(S)
    # Initialize an empty list to store the encrypted/decrypted characters
    res = []
    for c in text:
        # XOR operation between the current character and the next value from the keystream
        val = c ^ next(keystream)
        # Convert the resulting value to a character and add it to the result list
        res.append(val)
    # Join the characters in the result list and return the final encrypted/decrypted text
    output_text = ''.join(map(chr, res))
    return output_text, bytes(res)  # Return the output_text and the keystream as bytes

           