def affine_encrypt(plaintext, key):
    return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26) + ord('A')) for t in plaintext.upper().replace(' ', '') ])

plaintext = "Nguyen Dinh Minh Hieu"
key = [9, 2]
affine_cipher_text = affine_encrypt(plaintext, key)
print('Cipher Text: {}'.format(affine_cipher_text))