def matrix(x,y,initial):
    return [[initial for i in range(x)] for j in range(y)]
        
def encrypt():  #Encryption
    msg=str(input("ENTER MSG : "))
    msg=msg.upper()
    msg=msg.replace(" ", "")   
    key=input("Enter key : ")
    key=key.replace(" ", "")
    key=key.upper() 
       
    result=list()
    for c in key: #storing key in result
        if c not in result:
            if c=='J':
                result.append('I')
            else:
                result.append(c)
    flag=0
    for i in range(65,91): #storing other character in result
        if chr(i) not in result:            #Check for not repetition in matrix
            if i==73 and chr(74) not in result:
                result.append("I")
                flag=1
            elif flag==0 and i==73 or i==74:
                pass    
            else:
                result.append(chr(i))
    k=0
    my_matrix=matrix(5,5,0) #initialize matrix = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    for i in range(0,5): #making matrix and put the result in to the matrix to be encrypt or decrept
        for j in range(0,5):
            my_matrix[i][j]=result[k]
            k+=1

    def locindex(c): #get location of each character  
        loc=list()
        if c=='J':
            c='I'
        for i ,j in enumerate(my_matrix):
            for k,l in enumerate(j):
                if c==l:
                    loc.append(i)
                    loc.append(k)
                    return loc         
    i=0
    for s in range(0,len(msg)+1,2):
        if s<len(msg)-1:
            if msg[s]==msg[s+1]:
                msg=msg[:s+1]+'X'+msg[s+1:]
    if len(msg)%2!=0:   #check if msg is odd append ('x')
        msg=msg[:]+'X'
    print("CIPHER TEXT : ",end=' ')
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i])  #return each location of all elements in the msg in list
        loc1=list()
        loc1=locindex(msg[i+1])
        if loc[1]==loc1[1]:
            print("{}{}".format(my_matrix[(loc[0]+1)%5][loc[1]],
            my_matrix[(loc1[0]+1)%5][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(loc[1]+1)%5],
            my_matrix[loc1[0]][(loc1[1]+1)%5]),end=' ')  
        else:
            print("{}{}".format(my_matrix[loc[0]][loc1[1]],
            my_matrix[loc1[0]][loc[1]]),end=' ')    
        i=i+2        
                 
def decrypt():  #decryption
    msg=str(input("ENTER CIPHER TEXT : "))
    msg=msg.upper()
    msg=msg.replace(" ", "")   ################################3
    key=input("Enter key : ")
    key=key.replace(" ", "")
    key=key.upper()
    print("PLAIN TEXT : ",end=' ')
       
    result=list()
    for c in key: #storing key in result
        if c not in result:
            if c=='J':
                result.append('I')
            else:
                result.append(c)
    flag=0
    for i in range(65,91): #storing other character in result
        if chr(i) not in result:            #Check for not repetition in matrix
            if i==73 and chr(74) not in result:
                result.append("I")
                flag=1
            elif flag==0 and i==73 or i==74:
                pass    
            else:
                result.append(chr(i))
    k=0
    my_matrix=matrix(5,5,0) #initialize matrix = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    for i in range(0,5): #making matrix and put the result in to the matrix to be encrypt or decrept
        for j in range(0,5):
            my_matrix[i][j]=result[k]
            k+=1

    def locindex(c): #get location of each character   #########################3
        loc=list()
        if c=='J':
            c='I'
        for i ,j in enumerate(my_matrix):
            for k,l in enumerate(j):
                if c==l:
                    loc.append(i)
                    loc.append(k)
                    return loc
    i=0
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i])
        loc1=list()
        loc1=locindex(msg[i+1])
        if loc[1]==loc1[1]:
            print("{}{}".format(my_matrix[(loc[0]-1)%5][loc[1]],my_matrix[(loc1[0]-1)%5][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(loc[1]-1)%5],my_matrix[loc1[0]][(loc1[1]-1)%5]),end=' ')  
        else:
            print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]),end=' ')    
        i=i+2        
'''
while(1):
    choice=int(input("\n1.Encryption \n2.Decryption: \n3.EXIT \n"))
    if choice==1:
        encrypt()
    elif choice==2:
        decrypt()
    elif choice==3:
        exit()
    else:
        print("Choose correct choice")
'''