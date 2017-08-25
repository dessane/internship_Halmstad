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
	#Despite the other version, here, we will convert the word in binary before the mixing step
	#So we will have a word binary mixed instead of a word hexa mixed which is better because you won't be able to find hexa caracter in it which are present in the other version
	cipher_string=str(bin(int(cipher_string,16)))[2:]
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

#a need to be in binary
def decod_bazerie(a,k):
	cipher_string=""
	base=0
	str_complet=""
	x=True
	#Now we will mix the binary ciphered message to be able to decipher it
	while x==True:
		print("test")
		for indice in str(k):
			nb=int(indice)
			#We check that we don't have a length problem to mix it
			if(base<len(a)):
				#We check here that we won't try to mix outside of the message
				if(base+nb<len(a)):
					inv=a[base:base+nb]
				else:
					#If it's the end of the message we end the while
					inv=a[base:]
					x=False
				base=nb+base
				reverse=""
				#Here we will reverse the part of the word we took and then add it to the rest of the word
				for i in inv:
					reverse=i+reverse
				str_complet=str_complet+reverse
	
	#convert binary into hexa
	str_complet=str(hex(int(str_complet,2)))[2:]
	#We switch the two table
	tab_b=[["0","4","8","c"],["1","5","9","d"],["2","6","a","e"],["3","7","b","f"]]
	tab_a=[["5","a","7","2"],["0","f","4","b"],["3","8","d","c"],["e","1","6","9"]]
	#We will create the new word here by replacing the later by the the one in the other table
	for i in str_complet:
		line_n=0
		for line in tab_a:
			for ele in range(len(line)):
				if line[ele]==i:
					cipher_string+=tab_b[line_n][ele]
			line_n+=1

	return cipher_string

##code for k exchange##
#this function can be use to calcul X or k when you have Y, just replace g by Y
def k_value(n,g,x):
	return ((g**x)%n)

k=random.randint(10**(len(a)-1),(10**len(a))-1)
print(k)
print(a)
a_hex=str(hex(int(a,2)))[2:]
print(a_hex)
code=cod_bazerie(a_hex,k)
print(code)
print(decod_bazerie(code,k))
print("")
t_clear="10111001110100000111011001010101"
print(t_clear)
t_cipher=xor(t_clear,code)
print(t_cipher)
print(xor(t_cipher,code))



#Function which will try, if the message receive is not good, with other value of the noun to be check if the problem doesn't come from a difference in the counter.
def verif(m,a,liste_m):
	t=False
	a_hex=str(hex(int(a,2)))[2:]

	code=cod_bazerie(a_hex,k)
	m_d=xor(m,code)

	for msg in liste_m:
		if m_d==msg:
			t=True
			break
	if not t:
		a_num=int(a,2)
		liste_a[a-2,a-1,a+1,a+2]
		for i in liste_a:
			a_hex=str(hex(i))[2:]

			code=cod_bazerie(a_hex,k)
			m_d=xor(m,code)

			for msg in liste_m:
				if m_d==msg:
					t=True
					break
		
