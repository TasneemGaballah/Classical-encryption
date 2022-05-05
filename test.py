'''
print (ord('A'))
print ((( 9*(ord('W')+ord('A')) + 10 ) % 26)
				+ ord('A'))
print (ord('W')+ord('A'))
print (chr((( 9*(ord('W')+ord('A')) + 10 ) % 26)
				+ ord('A')))

print(chr((( 9*(ord('W')-ord('A')) + 10 ) % 26)))
print((( 9*(ord('W')-ord('A')) + 10 ) / 26))
'''
xorKey = 'C'
inpString = 'greek'
length = len(inpString)
for i in range(length):
	inpString = (chr(ord(inpString[i]) ^ ord(xorKey)))
	print (inpString[i])
	