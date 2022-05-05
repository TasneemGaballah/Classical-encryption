import affine
import ceasar
import playfair
import vernam as xor

while(1):
    print("\nWhich classical cryptog. method do you want?\n1.Ceasar cipher \n2.Affine cipher \n3.Playfair cipher \n4.XOR cipher\n5.EXIT \n")
    choice=int(input("Enter num:"))
    if choice==1:
        choice=int(input("\n1.Ceasar Encryption \n2.Decryption: \n3.EXIT\n"))
        if choice==1:
            ceasar.encrypt()
        elif choice==2:
           ceasar.decrypt()
        elif choice==3:
            exit()
        else:
            print("Choose correct choice")
    elif choice==2:
        choice=int(input("\n1.Affine Encryption \n2.Decryption: \n3.EXIT\n"))
        if choice==1:
            print("Cipher Text :",affine.affine_encrypt())
        elif choice==2:
            print("Plain Text :",affine.affine_decrypt())
        elif choice==3:
            exit()
        else:
            print("Choose correct choice")
    elif choice==3:
        choice=int(input("\n1.Playfair Encryption \n2.Decryption: \n3.EXIT\n"))
        if choice==1:
            playfair.encrypt()
        elif choice==2:
           playfair.decrypt()
        elif choice==3:
            exit()
        else:
            print("Choose correct choice")
    elif choice==4:
        choice=int(input("\n1.XOR Encryption \n2.Decryption: \n3.EXIT\n"))
        if choice==1:
            print("Cipher txt : ",xor.encryptDecrypt())
        elif choice==2:
           print("Plain txt : ",xor.encryptDecrypt())
        elif choice==3:
            exit()
    elif choice==5:
        exit()
    else:
        print("Choose correct choice")