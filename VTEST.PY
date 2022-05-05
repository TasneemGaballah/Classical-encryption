#implement XOR - Encryption
# The same function is used to encrypt and decrypt

def encryptDecrypt(inpString):
	# Define XOR key
	# Any character value will work
	xorKey = str(input("ENTER KEY : "))

	# calculate length of input string
	length = len(inpString)

	# perform XOR operation of key with every character in string
	for i in range(length):
		CT = ( chr(ord(inpString[i]) ^ ord(xorKey[i])))
		print(CT[i], end = "")
	return CT

# Driver Code
if __name__ == '__main__':
	sampleString = "BA1"

	# Encrypt the string
	print("Encrypted String: ", end = "")
	sampleString = encryptDecrypt(sampleString)
	print("\n")

	# Decrypt the string
	print("Decrypted String: ", end = "")
	encryptDecrypt(sampleString)

# This code is contributed by Princi Singh
