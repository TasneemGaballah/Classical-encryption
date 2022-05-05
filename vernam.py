#implement XOR - Encryption
# The same function is used to encrypt and decrypt

def encryptDecrypt():
    plain = str(input("ENTER Plain/cipher : "))
	# Define XOR key
	# Any character value will work
    xorKey = str(input("ENTER KEY : "))

	# calculate length of input string
    length = len(plain)

	# perform XOR operation of key with every character in string
    for i in range(length):
        cipher = (plain[:i] + chr(ord(plain[i]) ^ ord(xorKey[i])) + plain[i + 1:])
        #print(cipher[i], end = "")
    return cipher
''' 
# Driver Code
if __name__ == '__main__':
	
	# Encrypt the string
	print("Encrypted String: ", end = "")
	sampleString = encryptDecrypt(sampleString)
	print("\n")

	# Decrypt the string
	print("Decrypted String: ", end = "")
	encryptDecrypt(sampleString)

'''