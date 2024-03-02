def KeyMatrix(key):
    key = key.upper().replace(" ", "").replace("J","I") 
    key1 = []
    key_matrix = []
    for char in key:
        if char not in key1:
            key1.append(char)
    for char in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if char not in key1:
            key1.append(char)
    k = 0
    for i in range(5):
        row = []  
        for j in range(5):
            row.append(key1[i+j+k])  
        key_matrix.append(row) 
        k+=4 
    return key_matrix
def separate_same_letters(plaintext):
    index = 0
    while (index<len(plaintext)):
        l1 = plaintext[index]
        if index == len(plaintext)-1:
            plaintext = plaintext + 'X'
            index += 2
            continue
        l2 = plaintext[index+1]
        if l1==l2:
            plaintext = plaintext[:index+1] + "X" + plaintext[index+1:]
        index +=2   
    return plaintext
def indexOf(letter,matrix):
    for i in range (5):
        try:
            index = matrix[i].index(letter)
            return (i,index)
        except:
            continue
def playfair_encrypt(plaintext, key):
    matrix = KeyMatrix(key)
    plaintext = separate_same_letters(plaintext.upper().replace(' ','').replace('J','I'))     
    ciphertext=''
    for (l1, l2) in zip(plaintext[0::2], plaintext[1::2]):
        row1,col1 = indexOf(l1,matrix)
        row2,col2 = indexOf(l2,matrix)
        if row1==row2: 
            ciphertext += matrix[row1][(col1+1)%5] + matrix[row2][(col2+1)%5]
        elif col1==col2:
            ciphertext += matrix[(row1+1)%5][col1] + matrix[(row2+1)%5][col2]
        else: 
            ciphertext += matrix[row1][col2] + matrix[row2][col1]
    return ciphertext
key = "Nguyen Dinh Minh Hieu"
plaintext = "Hai Khong Hai Mot Khong Ba Bon Nam"
playfair_cipher_text = playfair_encrypt(plaintext, key)
print("Cipher Text: {}".format(playfair_cipher_text))

