def encrypt():
   text = input("Plain Text :")
   s = int(input("Enter key :"))
   result = ""
   # transverse the plain text
   for i in range(len(text)):
      char = text[i]
      # Encrypt uppercase characters in plain text     
      if (char.isupper()):
         result += chr((ord(char) + s-65) % 26 + 65)
      # Encrypt lowercase characters in plain text
      else:
         result += chr((ord(char) + s - 97) % 26 + 97)
   print ("Cipher Text : " + result)
def decrypt():
   cipher = input("Cipher Text :")
   k = int(input("Enter key :"))
   result = ""
   # transverse the cipher text
   for i in range(len(cipher)):
      char = cipher[i]
      # Decrypt uppercase characters in cipher text     
      if (char.isupper()):
         result += chr((ord(char) - k-65) % 26 + 65)
      # Decrypt lowercase characters in cipher text
      else:
         result += chr((ord(char) - k - 97) % 26 + 97)
   print ("Plain Text : " + result)
'''
while(1):
    choice=int(input("\n1.Encryption \n2.Decryption: \n3.EXIT\n"))
    if choice==1:
        encrypt()
    elif choice==2:
        decrypt()
    elif choice==3:
        exit()
    else:
        print("Choose correct choice")
'''