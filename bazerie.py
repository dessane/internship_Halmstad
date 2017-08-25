import random

a="11110110010101011011100111010111"


#take to string with a binary form
def xor(a,b):
	string=str(bin(int(a,2)^int(b,2)))
	return string[2:]

# a need to be in hexa
def cod_bazerie(a,k):
	cipher_string=""
	#Creation of the 2 table for the bazerie ciphering
	tab_a=[["0","4","8","c"],["1","5","9","d"],["2","6","a","e"],["3","7","b","f"]]
	tab_b=[["5","a","7","2"],["0","f","4","b"],["3","8","d","c"],["e","1","6","9"]]
	#We will create the new word here by replacing the later by the the one in the other table
	for i in a:
		line_n=0
		for line in tab_a:
			for ele in range(len(line)):
				if line[ele]==i:
					cipher_string+=tab_b[line_n][ele]
			line_n+=1
	print(cipher_string)
	base=0
	str_complet=""
	x=True
	#Now we will mix the ciphered message using the key k
	#While the whole message is not mixed we continue
	while x==True:
		for indice in str(k):
			nb=int(indice)
			#We check that we don't have a length problem to mix it
			if(base<len(cipher_string)):
				#We check here that we won't try to mix outside of the message
				if(base+nb<len(cipher_string)):
					inv=cipher_string[base:base+nb]
				else:
					#If it's the end of the message we end the while
					inv=cipher_string[base:]
					x=False
				base=nb+base
				reverse=""
				#Here we will reverse the part of the word we took and then add it to the rest of the word
				for i in inv:
					reverse=i+reverse
				str_complet=str_complet+reverse

	return str_complet


# a need to be in hexa
#To decipher the message, it's the same as the ciphering but we switch the table
def decod_bazerie(a,k):
	cipher_string=""
	tab_b=[["0","4","8","c"],["1","5","9","d"],["2","6","a","e"],["3","7","b","f"]]
	tab_a=[["5","a","7","2"],["0","f","4","b"],["3","8","d","c"],["e","1","6","9"]]
	for i in a:
		line_n=0
		for line in tab_a:
			for ele in range(len(line)):
				if line[ele]==i:
					cipher_string+=tab_b[line_n][ele]
			line_n+=1
	base=0
	str_complet=""
	x=True
	while x==True:
		for indice in str(k):
			nb=int(indice)
			if(base<len(cipher_string)):
				if(base+nb<len(cipher_string)):
					inv=cipher_string[base:base+nb]
				else:
					inv=cipher_string[base:]
					x=False
				base=nb+base
				reverse=""
				for i in inv:
					reverse=i+reverse
				str_complet=str_complet+reverse
	return str_complet


##code for k exchange##
#this function can be use to calcul X or k when you have Y, just replace g by Y
#useful for Diffie-Hellman protocol
def k_value(n,g,x):
	return ((g**x)%n)

#We create the key so she is long enough to be sure to match the length of the message
k=random.randint(10**(len(a)-1),(10**len(a))-1)
print(k)
print(a)
#We convert the binary message into a int that we convert into hexa
#after that we convert it into a string where we will delete the two first character which are not useful here
a_hex=str(hex(int(a,2)))[2:]
print(a_hex)
code=cod_bazerie(a_hex,k)
print(code)
a_code=str(bin(int(code,16)))[2:]

print(a_code)

#we will try the xor with the ciphered message to see if everything works
t_clear="10111001110100000111011001010101"
print(t_clear)
t_cipher=xor(t_clear,a_code)
print(t_cipher)
print(xor(t_cipher,a_code))

#We will then try to decipher it to see if we find the message frome the beginning
decod=decod_bazerie(code,k)

print(str(bin(int(decod,16)))[2:])

