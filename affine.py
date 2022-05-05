# Implementation of Affine Cipher in Python
# Extended Euclidean Algorithm for finding modular inverse
def egcd(a, b):
	x,y, u,v = 0,1, 1,0         #x=0,y=1,u=1,v=0
	while a != 0:
		q, r = b//a, b%a        #q=b/a , r=b%a
		m, n = x-u*q, y-v*q
		b,a, x,y, u,v = a,r, u,v, m,n
	gcd = b
	return gcd, x, y

def modinv(a, m):
	gcd, x, y = egcd(a, m)
	if gcd != 1:
		return None # modular inverse does not exist
	else:
		return x % m


# affine cipher encryption function
# returns the cipher text
def affine_encrypt():
    plain = str(input("Plain Text :"))
    key = int(input("Enter key :"))
    m = int(input("Enter multi.factor :"))
	#C = (a*P + b) % 26
    return ''.join([ chr((( m*(ord(t)-ord('A')) + key ) % 26)
				+ ord('A')) for t in plain.upper().replace(' ', '') ]) 


# affine cipher decryption function
# returns original text
def affine_decrypt():
     cipher = str(input("Cipher Text :"))
     key= int(input("Enter key :"))
     m= int(input("Enter multi.factor :"))
	#P = (a^-1 * (C - b)) % 26	
     return ''.join([ chr((( modinv(m, 26)*(ord(c)-ord('A')- key))
					% 26) + ord('A')) for c in cipher.upper().replace(' ', '') ])

# Driver Code to test the above functions
'''
while(1):
    choice=int(input("\n1.Encryption \n2.Decryption: \n3.EXIT\n"))
    if choice==1:
        print("Cipher Text :",affine_encrypt())
    elif choice==2:
        print("Plain Text :",affine_decrypt())
    elif choice==3:
        exit()
    else:
        print("Choose correct choice")
'''        


    
