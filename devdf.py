#Without prebuilt function in python

def printVowels(cadena,character):
	count = 0  
	for e in "".join(sorted(cadena)):
	  	if ord(e) <= ord('e'): 
	  		if ord(e) == ord(character):  
	  	 	 		count = count + 1
	  	else:
	  		break
	return count

def reverse(cadena):
	l = [] 
	reverseS = ""
	for a in cadena:
		l.append(a)
	while l:
		 reverseS = reverseS +(l.pop())
	return reverseS

print(reverse('El DevF rockea'))
print(printVowels('reverseS','e'))